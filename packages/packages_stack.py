from aws_cdk import (
    Duration,
    RemovalPolicy,
    Size,
    Stack,
    aws_events as _events,
    aws_events_targets as _targets,
    aws_iam as _iam,
    aws_lambda as _lambda,
    aws_logs as _logs,
    aws_s3 as _s3,
    aws_ssm as _ssm
)

from constructs import Construct

class PackagesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

    ### ODIC ###

        provider = _iam.OpenIdConnectProvider(
            self, 'provider',
            url = 'https://token.actions.githubusercontent.com',
            client_ids = [
                'sts.amazonaws.com'
            ]
        )

        github = _iam.Role(
            self, 'github',
            assumed_by = _iam.WebIdentityPrincipal(provider.open_id_connect_provider_arn).with_conditions(
                {
                    'StringLike': {
                        'token.actions.githubusercontent.com:sub': 'repo:jblukach/packages:*'
                    }
                }
            )            
        )

    ### LAYER ###

        pkgpip = _ssm.StringParameter.from_string_parameter_attributes(
            self, 'pkgpip',
            parameter_name = '/pkg/pip'
        )

        pip = _lambda.LayerVersion.from_layer_version_arn(
            self, 'pip',
            layer_version_arn = pkgpip.string_value
        )

    ### BUCKETS ###

        use1bucket = _s3.Bucket.from_bucket_name(
            self, 'use1',
            bucket_name = 'pylambdapkgsuse1'
        )

        use2bucket = _s3.Bucket.from_bucket_name(
            self, 'use2',
            bucket_name = 'pylambdapkgsuse2'
        )

        usw2bucket = _s3.Bucket.from_bucket_name(
            self, 'usw2',
            bucket_name = 'pylambdapkgsusw2'
        )

    ### IAM ###

        role = _iam.Role(
            self, 'role', 
            assumed_by = _iam.ServicePrincipal(
                'lambda.amazonaws.com'
            )
        )

        role.add_managed_policy(
            _iam.ManagedPolicy.from_aws_managed_policy_name(
                'service-role/AWSLambdaBasicExecutionRole'
            )
        )

        role.add_to_policy(
            _iam.PolicyStatement(
                actions = [
                    'ssm:PutParameter'
                ],
                resources = [
                    '*'
                ]
            )
        )

        role.add_to_policy(
            _iam.PolicyStatement(
                actions = [
                    's3:PutObject'
                ],
                resources = [
                    use1bucket.arn_for_objects('*'),
                    use2bucket.arn_for_objects('*'),
                    usw2bucket.arn_for_objects('*')
                ]
            )
        )

    ### LAMBDA ###

        download = _lambda.Function(
            self, 'download',
            runtime = _lambda.Runtime.PYTHON_3_13,
            architecture = _lambda.Architecture.ARM_64,
            code = _lambda.Code.from_asset('download'),
            handler = 'download.handler',
            environment = dict(
                USE1 = use1bucket.bucket_name,
                USE2 = use2bucket.bucket_name,
                USW2 = usw2bucket.bucket_name
            ),
            ephemeral_storage_size = Size.gibibytes(2),
            timeout = Duration.seconds(900),
            memory_size = 2048,
            role = role,
            layers = [
                pip
            ]
        )

        logs = _logs.LogGroup(
            self, 'logs',
            log_group_name = '/aws/lambda/'+download.function_name,
            retention = _logs.RetentionDays.ONE_WEEK,
            removal_policy = RemovalPolicy.DESTROY
        )

        event = _events.Rule(
            self, 'event',
            schedule = _events.Schedule.cron(
                minute = '0',
                hour = '0',
                month = '1',
                week_day = '*',
                year = '*'
            )
        )

        event.add_target(
            _targets.LambdaFunction(download)
        )
