#!/usr/bin/env node

/********** how to use **********
1. Initialize the package working directory
> npm -y init

2.Install minio package 
> npm install minio

3. Have your end-point, access-key, secret-key from your provider (e.g. poshtiban.com)

4. Assign your credentials to variables to be picked up by nodejs ENV variable
export END_POINT=<your-end-point>
export ACCESS_KEY=<your-access-key>
export SECRET_KEY=<your-secret-key>

5. Run it
node index.js

5.1  Or run it as a one-liner 
END_POINT=<your-end-point> ACCESS_KEY=<your-access-key> SECRET_KEY=<your-secret-key> node index.js

As a one-liner sample
END_POINT=<s3.example.com> ACCESS_KEY=<t7XViGJK3LaKMhj9> SECRET_KEY=<q7lfyrT5qMHgsCle2DJzUtajsm5xvJrz> node index.js

*/

/********** reference **********
https://docs.min.io/docs/javascript-client-api-reference.html#listBuckets
*/

const Minio = require('minio')

const log = console.log.bind( console );

// constructor
const mc = new Minio.Client({
    endPoint: process.env.END_POINT,
    port: 443,
    useSSL: true,
    accessKey: process.env.ACCESS_KEY,
    secretKey: process.env.SECRET_KEY
});

// get list of buckets
mc.listBuckets( function( error, buckets ){
    if( error ){
        return log( error );
    }
    
    // see list of buckets
    for( const obj of buckets ) {
       log( 'name / date:', obj.name, obj.creationDate  );
    }
});
