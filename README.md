# miniml
A minimal application design pattern for data science models

## Goal
Provide a way to deliver data science predictions to an unknown number of downstream systems or applications with high reliability and low toil.

## Project structure
All relevant files for running the application are located in the `src` directory. This is mainly so that during the build process for creating an image to run the application, the context directory can be set to `src` so that only these files are included in the image; any notebooks, documentation, reference material, or other items related to the project in other directories could be excluded from the build process so that they aren't needlessly copied and don't use resources in the production system.

To run the application locally, navigate to the `src` directory and run `server.py`:
```bash
cd src
python server.py
```

Testing
