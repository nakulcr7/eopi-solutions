## Notes:
---------
- x & (x - 1) sets erases the lowest set bit. Similary, x & ~(x - 1) isolates the lowest set bit of x.
- The parity of <b63, b62, ..., b0> is the parity of xor(<b63...b32>, <b31, b0>) and so on recursively.