from aws_cdk import (
    RemovalPolicy,
    Stack,
    aws_lambda as _lambda,
    aws_s3 as _s3,
    aws_ssm as _ssm
)

from constructs import Construct

class PackagesLayersUSE2(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        orgid = _ssm.StringParameter.from_string_parameter_attributes(
            self, 'orgid',
            parameter_name = '/org/id'
        )

    ### BUCKET ###

        bucket = _s3.Bucket(
            self, 'bucket',
            bucket_name = 'pylambdapkgsuse2',
            encryption = _s3.BucketEncryption.S3_MANAGED,
            block_public_access = _s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy = RemovalPolicy.DESTROY,
            auto_delete_objects = True,
            enforce_ssl = True,
            versioned = False
        )

    ### PARAMETERS ###

        updatedbeautifulsoup4 = _ssm.StringParameter(
            self, 'updatedbeautifulsoup4',
            parameter_name = '/updated/beautifulsoup4',
            string_value = 'EMPTY',
            tier = _ssm.ParameterTier.STANDARD
        )

        updatedcensys = _ssm.StringParameter(
            self, 'updatedcensys',
            parameter_name = '/updated/censys',
            string_value = 'EMPTY',
            tier = _ssm.ParameterTier.STANDARD
        )

        updateddnspython = _ssm.StringParameter(
            self, 'updateddnspython',
            parameter_name = '/updated/dnspython',
            string_value = 'EMPTY',
            tier = _ssm.ParameterTier.STANDARD
        )

        updatedgeoip2 = _ssm.StringParameter(
            self, 'updatedgeoip2',
            parameter_name = '/updated/geoip2',
            string_value = 'EMPTY',
            tier = _ssm.ParameterTier.STANDARD
        )

        updatedmaxminddb = _ssm.StringParameter(
            self, 'updatedmaxminddb',
            parameter_name = '/updated/maxminddb',
            string_value = 'EMPTY',
            tier = _ssm.ParameterTier.STANDARD
        )

        updatednetaddr = _ssm.StringParameter(
            self, 'updatednetaddr',
            parameter_name = '/updated/netaddr',
            string_value = 'EMPTY',
            tier = _ssm.ParameterTier.STANDARD
        )

        updatedpip = _ssm.StringParameter(
            self, 'updatedpip',
            parameter_name = '/updated/pip',
            string_value = 'EMPTY',
            tier = _ssm.ParameterTier.STANDARD
        )

        updatedrequests = _ssm.StringParameter(
            self, 'updatedrequests',
            parameter_name = '/updated/requests',
            string_value = 'EMPTY',
            tier = _ssm.ParameterTier.STANDARD
        )

        updatedsmartopen = _ssm.StringParameter(
            self, 'updatedsmartopen',
            parameter_name = '/updated/smartopen',
            string_value = 'EMPTY',
            tier = _ssm.ParameterTier.STANDARD
        )

    ### beautifulsoup4 LAYER ###
    ### censys LAYER ###
    ### dnspython LAYER ###
    ### geoip2 LAYER ###
    ### maxminddb LAYER ###
    ### netaddr LAYER ###

    ### pip LAYER ###

        pipstatus = _ssm.StringParameter.from_string_parameter_attributes(
            self, 'pipstatus',
            parameter_name = '/updated/pip'
        )

        pkgpip = _lambda.LayerVersion(
            self, 'pkgpip',
            layer_version_name = 'pkgpip',
            description = pipstatus.string_value,
            code = _lambda.Code.from_bucket(
                bucket = bucket,
                key = 'pip.zip'
            ),
            compatible_architectures = [
                _lambda.Architecture.ARM_64,
                _lambda.Architecture.X86_64
            ],
            compatible_runtimes = [
                _lambda.Runtime.PYTHON_3_9,
                _lambda.Runtime.PYTHON_3_10,
                _lambda.Runtime.PYTHON_3_11,
                _lambda.Runtime.PYTHON_3_12,
                _lambda.Runtime.PYTHON_3_13
            ],
            removal_policy = RemovalPolicy.DESTROY
        )

        ssmpip = _ssm.StringParameter(
            self, 'ssmpip',
            parameter_name = '/pkg/pip',
            string_value = pkgpip.layer_version_arn,
            tier = _ssm.ParameterTier.STANDARD
        )

    ### requests LAYER ###
    ### smartopen LAYER ###
