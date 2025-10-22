```mermaid
flowchart LR
    subgraph "Universal Set (Ω)"
        style Universal fill:#f5f5f5,stroke:#333,stroke-width:2px
        
        subgraph "A"
            style A fill:#FF8888,stroke:#FF0000,stroke-width:2px,opacity:0.7
            A_only["A - B"]
            style A_only fill:#FF8888,stroke:none,opacity:0.7,color:white
        end
        
        subgraph "B"
            style B fill:#88AAFF,stroke:#0044FF,stroke-width:2px,opacity:0.7
            B_only["B - A"]
            style B_only fill:#88AAFF,stroke:none,opacity:0.7,color:white
        end
        
        subgraph "A ∩ B"
            style "A ∩ B" fill:#B878DD,stroke:none,stroke-width:2px,opacity:0.9
            intersection["A ∩ B"]
            style intersection fill:#B878DD,stroke:none,opacity:0.9,color:white
        end
        
        outside["Ωc"]
        style outside fill:#f5f5f5,stroke:none,opacity:0.5
        
        %% Set up positions to create Venn diagram appearance
        A ~~~ "A ∩ B"
        B ~~~ "A ∩ B"
        "A ∩ B" ~~~ outside
    end

    %% Add legend for set operations
    subgraph "Set Operations"
        style "Set Operations" fill:#ffffff,stroke:#333,stroke-width:1px
        op1["A ∪ B: Union"]
        op2["A ∩ B: Intersection"]
        op3["Ac: Complement"]
        op4["A - B: Difference"]
        style op1 fill:#ffffff,stroke:none
        style op2 fill:#ffffff,stroke:none
        style op3 fill:#ffffff,stroke:none
        style op4 fill:#ffffff,stroke:none
    end
```
