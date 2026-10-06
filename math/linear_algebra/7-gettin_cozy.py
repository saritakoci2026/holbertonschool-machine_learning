#!/usr/bin/env python3
"""Concatenate two 2D matrices."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenate two 2D matrices along a given axis."""
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None

        result = []
        for row in mat1:
            result.append(row.copy())
        for row in mat2:
            result.append(row.copy())

        return result

    if axis == 1:
        if len(mat1) != len(mat2):
            return None

        result = []
        for i in range(len(mat1)):
            result.append(mat1[i].copy() + mat2[i].copy())

        return result

    return None
