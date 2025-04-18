# DataBinder

This project aims to:

1. Provide a general framework for creating, exploring and converting 'reaction
   graphs'.
2. interface experimental conditions and data with models designed to describe
   them.

One of the key processes in modelling is to make sure that the model is designed
within the parameters of the data it is designed to model. For example, does the
model contain the variables given in the data? Does the model cover the correct
time period for a time series? Is the model compatible with the data? These
questions are rather mechanical: once the model has been selected, and the data
specified, it is trivial to make sure that they are compatible.

## Usage

Navigate into the DataBinder root directory, and run `pip install -e .`.

See `test.py` and `example_data` for the functionality covered in this package.

API documentation is also available in the `doc` folder (once you have the files
on your computer, open `docs/index.html` in your web browser).

## Theory

Topological information is represented as a series of transformations,
represented as, for example:

```
A.B>>C
C>>D.E
```

Above, 'entities' `A` and `B` are required for the *transformation* which creates
*entity* `C`. Similarly, `C` is required for a transformation which creates `D`
and `E`.

There is a prototype sketch of a validation procedure which tests for
compatibility between topologies and data.

Simple Python functions can be created from topologies, as well as adjacency
matrices.
