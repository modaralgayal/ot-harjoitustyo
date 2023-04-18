# Arkkitehtuuri 


```mermaid

flowchart TD;

    Renderer(Renderer)
    GameLoop(Gameloop)
    Main(Main)

    Renderer --> GameLoop
    GameLoop --> Main
    Renderer --> Main

```