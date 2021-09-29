<?php

// Include the SDK using the Composer autoloader
date_default_timezone_set('America/Los_Angeles');
require 'vendor/autoload.php';

$s3 = new Aws\S3\S3Client([
        'version' => 'latest',
        'region'  => 'us-east-1',
        'endpoint' => 'https://s3w-shakibamoshiri.s3.ir-west-1.poshtiban.com',
        'use_path_style_endpoint' => true,
        'credentials' => [
                'key'    => 't7XViGJK3LaKMhj9',
                'secret' => 'q7lfyrT5qMHgsCle2DJzUtajsm5xvJrz',
            ],
]);

$buckets = $s3->listBuckets();

foreach ($buckets['Buckets'] as $bucket) {
    echo $bucket['Name'] . "\n";
}

?>
