from aws_cdk import (
    RemovalPolicy,
    Stack,
    aws_iam as _iam,
    aws_lambda as _lambda,
    aws_ram as _ram,
    aws_s3 as _s3,
    aws_ssm as _ssm
)

from constructs import Construct

class PackagesLayersUSE1(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        orgid = _ssm.StringParameter.from_string_parameter_attributes(
            self, 'orgid',
            parameter_name = '/org/id'
        )

    ### BUCKET ###

        bucket = _s3.Bucket(
            self, 'bucket',
            bucket_name = 'pylambdapkgsuse1',
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

        beautifulsoup4status = _ssm.StringParameter.from_string_parameter_attributes(
            self, 'beautifulsoup4status',
            parameter_name = '/updated/beautifulsoup4'
        )

        pkgbeautifulsoup4 = _lambda.LayerVersion(
            self, 'pkgbeautifulsoup4',
            layer_version_name = 'pkgbeautifulsoup4',
            description = beautifulsoup4status.string_value,
            code = _lambda.Code.from_bucket(
                bucket = bucket,
                key = 'beautifulsoup4.zip'
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

        ssmbeautifulsoup4 = _ssm.StringParameter(
            self, 'ssmbeautifulsoup4',
            parameter_name = '/pkg/beautifulsoup4',
            string_value = pkgbeautifulsoup4.layer_version_arn,
            tier = _ssm.ParameterTier.ADVANCED
        )

        pkgbeautifulsoup4.add_permission(
            id = 'permissionbeautifulsoup4',
            account_id = '*',
            organization_id = orgid.string_value
        )

    ### censys LAYER ###

        censysstatus = _ssm.StringParameter.from_string_parameter_attributes(
            self, 'censysstatus',
            parameter_name = '/updated/censys'
        )

        pkgcensys = _lambda.LayerVersion(
            self, 'pkgcensys',
            layer_version_name = 'pkgcensys',
            description = censysstatus.string_value,
            code = _lambda.Code.from_bucket(
                bucket = bucket,
                key = 'censys.zip'
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

        ssmcensys = _ssm.StringParameter(
            self, 'ssmcensys',
            parameter_name = '/pkg/censys',
            string_value = pkgcensys.layer_version_arn,
            tier = _ssm.ParameterTier.ADVANCED
        )

        pkgcensys.add_permission(
            id = 'permissioncensys',
            account_id = '*',
            organization_id = orgid.string_value
        )

    ### dnspython LAYER ###

        dnspythonstatus = _ssm.StringParameter.from_string_parameter_attributes(
            self, 'dnspythonstatus',
            parameter_name = '/updated/dnspython'
        )

        pkgdnspython = _lambda.LayerVersion(
            self, 'pkgdnspython',
            layer_version_name = 'pkgdnspython',
            description = dnspythonstatus.string_value,
            code = _lambda.Code.from_bucket(
                bucket = bucket,
                key = 'dnspython.zip'
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

        ssmdnspython = _ssm.StringParameter(
            self, 'ssmdnspython',
            parameter_name = '/pkg/dnspython',
            string_value = pkgdnspython.layer_version_arn,
            tier = _ssm.ParameterTier.ADVANCED
        )

        pkgdnspython.add_permission(
            id = 'permissiondnspython',
            account_id = '*',
            organization_id = orgid.string_value
        )

    ### geoip2 LAYER ###

        geoip2status = _ssm.StringParameter.from_string_parameter_attributes(
            self, 'geoip2status',
            parameter_name = '/updated/geoip2'
        )

        pkggeoip2 = _lambda.LayerVersion(
            self, 'pkggeoip2',
            layer_version_name = 'pkggeoip2',
            description = geoip2status.string_value,
            code = _lambda.Code.from_bucket(
                bucket = bucket,
                key = 'geoip2.zip'
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

        ssmgeoip2 = _ssm.StringParameter(
            self, 'ssmgeoip2',
            parameter_name = '/pkg/geoip2',
            string_value = pkggeoip2.layer_version_arn,
            tier = _ssm.ParameterTier.ADVANCED
        )

        pkggeoip2.add_permission(
            id = 'permissiongeoip2',
            account_id = '*',
            organization_id = orgid.string_value
        )

    ### maxminddb LAYER ###

        maxminddbstatus = _ssm.StringParameter.from_string_parameter_attributes(
            self, 'maxminddbstatus',
            parameter_name = '/updated/maxminddb'
        )

        pkgmaxminddb = _lambda.LayerVersion(
            self, 'pkgmaxminddb',
            layer_version_name = 'pkgmaxminddb',
            description = maxminddbstatus.string_value,
            code = _lambda.Code.from_bucket(
                bucket = bucket,
                key = 'maxminddb.zip'
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

        ssmmaxminddb = _ssm.StringParameter(
            self, 'ssmmaxminddb',
            parameter_name = '/pkg/maxminddb',
            string_value = pkgmaxminddb.layer_version_arn,
            tier = _ssm.ParameterTier.ADVANCED
        )

        pkgmaxminddb.add_permission(
            id = 'permissionmaxminddb',
            account_id = '*',
            organization_id = orgid.string_value
        )

    ### netaddr LAYER ###

        netaddrstatus = _ssm.StringParameter.from_string_parameter_attributes(
            self, 'netaddrstatus',
            parameter_name = '/updated/netaddr'
        )

        pkgnetaddr = _lambda.LayerVersion(
            self, 'pkgnetaddr',
            layer_version_name = 'pkgnetaddr',
            description = netaddrstatus.string_value,
            code = _lambda.Code.from_bucket(
                bucket = bucket,
                key = 'netaddr.zip'
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

        ssmnetaddr = _ssm.StringParameter(
            self, 'ssmnetaddr',
            parameter_name = '/pkg/netaddr',
            string_value = pkgnetaddr.layer_version_arn,
            tier = _ssm.ParameterTier.ADVANCED
        )

        pkgnetaddr.add_permission(
            id = 'permissionnetaddr',
            account_id = '*',
            organization_id = orgid.string_value
        )

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

        requestsstatus = _ssm.StringParameter.from_string_parameter_attributes(
            self, 'requestsstatus',
            parameter_name = '/updated/requests'
        )

        pkgrequests = _lambda.LayerVersion(
            self, 'pkgrequests',
            layer_version_name = 'pkgrequests',
            description = requestsstatus.string_value,
            code = _lambda.Code.from_bucket(
                bucket = bucket,
                key = 'requests.zip'
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

        ssmrequests = _ssm.StringParameter(
            self, 'ssmrequests',
            parameter_name = '/pkg/requests',
            string_value = pkgrequests.layer_version_arn,
            tier = _ssm.ParameterTier.ADVANCED
        )

        pkgrequests.add_permission(
            id = 'permissionrequests',
            account_id = '*',
            organization_id = orgid.string_value
        )

    ### smartopen LAYER ###

        smartopenstatus = _ssm.StringParameter.from_string_parameter_attributes(
            self, 'smartopenstatus',
            parameter_name = '/updated/smartopen'
        )

        pkgsmartopen = _lambda.LayerVersion(
            self, 'pkgsmartopen',
            layer_version_name = 'pkgsmartopen',
            description = smartopenstatus.string_value,
            code = _lambda.Code.from_bucket(
                bucket = bucket,
                key = 'smartopen.zip'
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

        ssmsmartopen = _ssm.StringParameter(
            self, 'ssmsmartopen',
            parameter_name = '/pkg/smartopen',
            string_value = pkgsmartopen.layer_version_arn,
            tier = _ssm.ParameterTier.ADVANCED
        )

        pkgsmartopen.add_permission(
            id = 'permissionsmartopen',
            account_id = '*',
            organization_id = orgid.string_value
        )

    ### RAM ###

        share = _ram.CfnResourceShare(
            self, 'share',
            name = 'packages',
            allow_external_principals = False,
            permission_arns = [
                'arn:aws:ram::aws:permission/AWSRAMDefaultPermissionSSMParameterReadOnly'
            ],
            principals = [
                account
            ],
            resource_arns = [
                ssmbeautifulsoup4.parameter_arn,
                ssmcensys.parameter_arn,
                ssmdnspython.parameter_arn,
                ssmgeoip2.parameter_arn,
                ssmmaxminddb.parameter_arn,
                ssmnetaddr.parameter_arn,
                ssmrequests.parameter_arn,
                ssmsmartopen.parameter_arn
            ]
        )
