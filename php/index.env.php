<?php

// Include the SDK using the Composer autoloader
date_default_timezone_set('America/Los_Angeles');
require 'vendor/autoload.php';

$s3 = new Aws\S3\S3Client([
        'version' => 'latest',
        'region'  => 'us-east-1',
        'endpoint' => getenv['END_POINT'],
        'use_path_style_endpoint' => true,
        'credentials' => [
                'key'    =>  getenv['ACCESS_KEY'],
                'secret' => getenv['SECRET_KEY'],
            ],
]);

$buckets = $s3->listBuckets();

foreach ($buckets['Buckets'] as $bucket) {
    echo $bucket['Name'] . "\n";
}

?>
