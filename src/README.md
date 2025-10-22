# Set Operations Diagram Generator

This directory contains scripts for generating visualization diagrams for set operations using Python with matplotlib and matplotlib-venn.

## Requirements

- Python 3.6 or higher
- Matplotlib
- matplotlib-venn
- NumPy

## Setup

The dependencies can be installed using pip:

```bash
pip install -r requirements.txt
```

## Usage

### Automatic Generation

Run the provided shell script to generate all diagrams automatically:

```bash
./generate_diagrams.sh
```

This will create all the diagrams and save them in the `../book/figures/set_operations/` directory.

### Manual Generation

You can also run the Python script directly:

```bash
python3 generate_set_operations.py
```

## Generated Diagrams

The script generates the following set operation diagrams:

1. Intersection (A ∩ B)
2. Union (A ∪ B)
3. Set Difference (A \ B)
4. Subset (B ⊂ A)
5. Complement (A^c)
6. Disjoint Sets
7. Partition of Ω
8. Symmetric Difference (A △ B)
9. Combined figure with all operations

## Integration with LaTeX

To include these images in your LaTeX document, you can use the `\includegraphics` command:

```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.7\textwidth]{figures/set_operations/intersection.png}
    \caption{Intersection of sets A and B}
    \label{fig:intersection}
\end{figure}
```

Or you can create a figure with multiple subfigures:

```latex
\begin{figure}[h]
    \centering
    \begin{subfigure}{0.45\textwidth}
        \includegraphics[width=\textwidth]{figures/set_operations/intersection.png}
        \caption{Intersection: $A \cap B$}
    \end{subfigure}
    \hfill
    \begin{subfigure}{0.45\textwidth}
        \includegraphics[width=\textwidth]{figures/set_operations/union.png}
        \caption{Union: $A \cup B$}
    \end{subfigure}
    \caption{Basic set operations}
    \label{fig:set-operations}
\end{figure}
```

Alternatively, you can use the combined figure:

```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=\textwidth]{figures/set_operations/all_operations.png}
    \caption{Visualization of fundamental set operations}
    \label{fig:all-set-operations}
\end{figure}
```
