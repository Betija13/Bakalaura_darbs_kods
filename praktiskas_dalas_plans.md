```mermaid
flowchart LR
    subgraph 0i1[apmāca]
    direction LR
    A[Runātājs 1 Lasa tekstu] --> B[STT modelis] --> C[Transkripts 1]
    end
```
```mermaid
flowchart LR
    subgraph inference
    direction LR
    D[Runātājs 2 Lasa tekstu] --> E[STT modelis] --> F[Transkripts 2]
    end
    
```
```mermaid
flowchart LR
    subgraph zid[apmāca]
    direction LR
    id2[Runātājs 2 Lasa tekstu] --> id3[SST modelis]
    id0[Runātāja 1 stila vektors] --> id3
    end
    
    id3 -- inference --> id5[STT modelis] 
    
    id5[STT modelis] --> id4[Transkripts 3]
    
```
Mērķis: samazināt CER/WER Transkriptam 3 attiecībā pret Transkriptu 2

STT - Speech to text

SST - Speech style transfer