#!/usr/bin/env python3
import os

import aws_cdk as cdk

from packages.packages_layersuse1 import PackagesLayersUSE1
from packages.packages_layersuse2 import PackagesLayersUSE2
from packages.packages_layersusw2 import PackagesLayersUSW2
from packages.packages_stack import PackagesStack

app = cdk.App()

PackagesStack(
    app, 'PackagesStack',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

PackagesLayersUSE1(
    app, 'PackagesLayersUSE1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

PackagesLayersUSE2(
    app, 'PackagesLayersUSE2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

PackagesLayersUSW2(
    app, 'PackagesLayersUSW2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-west-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

cdk.Tags.of(app).add('Alias','Extensions')
cdk.Tags.of(app).add('GitHub','https://github.com/jblukach/packages')

app.synth()