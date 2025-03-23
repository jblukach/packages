# packages

### Cloud Development Kit (CDK)

```python
    ### LAMBDA LAYER ###

        pkgrequests = _ssm.StringParameter.from_string_parameter_arn(
            self, 'pkgrequests',
            'arn:aws:ssm:us-east-1:070176467818:parameter/pkg/requests'
        )

        requests = _lambda.LayerVersion.from_layer_version_arn(
            self, 'requests',
            layer_version_arn = pkgrequests.string_value
        )
```

## Lambda Layers

### USE1

```
arn:aws:ssm:us-east-1:070176467818:parameter/pkg/beautifulsoup4
arn:aws:ssm:us-east-1:070176467818:parameter/pkg/censys
arn:aws:ssm:us-east-1:070176467818:parameter/pkg/dnspython
arn:aws:ssm:us-east-1:070176467818:parameter/pkg/geoip2
arn:aws:ssm:us-east-1:070176467818:parameter/pkg/maxminddb
arn:aws:ssm:us-east-1:070176467818:parameter/pkg/netaddr
arn:aws:ssm:us-east-1:070176467818:parameter/pkg/requests
arn:aws:ssm:us-east-1:070176467818:parameter/pkg/smartopen
```

### USE2

```
arn:aws:ssm:us-east-2:070176467818:parameter/pkg/beautifulsoup4
arn:aws:ssm:us-east-2:070176467818:parameter/pkg/censys
arn:aws:ssm:us-east-2:070176467818:parameter/pkg/dnspython
arn:aws:ssm:us-east-2:070176467818:parameter/pkg/geoip2
arn:aws:ssm:us-east-2:070176467818:parameter/pkg/maxminddb
arn:aws:ssm:us-east-2:070176467818:parameter/pkg/netaddr
arn:aws:ssm:us-east-2:070176467818:parameter/pkg/requests
arn:aws:ssm:us-east-2:070176467818:parameter/pkg/smartopen
```

### USW2

```
arn:aws:ssm:us-west-2:070176467818:parameter/pkg/beautifulsoup4
arn:aws:ssm:us-west-2:070176467818:parameter/pkg/censys
arn:aws:ssm:us-west-2:070176467818:parameter/pkg/dnspython
arn:aws:ssm:us-west-2:070176467818:parameter/pkg/geoip2
arn:aws:ssm:us-west-2:070176467818:parameter/pkg/maxminddb
arn:aws:ssm:us-west-2:070176467818:parameter/pkg/netaddr
arn:aws:ssm:us-west-2:070176467818:parameter/pkg/requests
arn:aws:ssm:us-west-2:070176467818:parameter/pkg/smartopen
```

## SSM Parameters

### USE1

```
arn:aws:ssm:us-east-1:070176467818:parameter/root/account
arn:aws:ssm:us-east-1:070176467818:parameter/root/organization
```

### USE2

```
arn:aws:ssm:us-east-2:070176467818:parameter/root/account
arn:aws:ssm:us-east-2:070176467818:parameter/root/organization
```

### USW2

```
arn:aws:ssm:us-west-2:070176467818:parameter/root/account
arn:aws:ssm:us-west-2:070176467818:parameter/root/organization
```
