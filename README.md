# Videogrammetry

This repository contains scripts to convert a video of 3d real life objects or places in 3d model using videogrammetry.

#### The main python script has the following algorithm:
1. User input the required data
2. Make a post request to the spectre3D api with the input video file.
3. Make a get request to spectre3D api to get the status of the processing.
4. If successfully processed, run the javascript program to upload the 3D model generated to the ipfs.
5. After sucessfull upload, we get a confirmation message. 

## To run the script:
    python run_api.py

## To upload a custom file to the IPFS:
    node web3-client.js --token=<api-token> <file>
