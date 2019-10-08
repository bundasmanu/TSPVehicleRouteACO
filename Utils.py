
class Utils:

    INITIALPOINT = "nodoInicial"
    FINALPOINT = "nodoFinal"
    FEROMONERATE = "taxaFeromona"
    DISTANCE = "distancia"
    EDGES = "edges"

    dict={INITIALPOINT : 'A', EDGES : {
                                    {INITIALPOINT: 'A', FINALPOINT: 'B', DISTANCE: 2, FEROMONERATE : 0.1},
                                    {INITIALPOINT: 'A', FINALPOINT: 'C', DISTANCE: 5, FEROMONERATE: 0.1},
                                    {INITIALPOINT: 'A', FINALPOINT: 'D', DISTANCE: 5, FEROMONERATE: 0.2},
                                    {INITIALPOINT: 'A', FINALPOINT: 'E', DISTANCE: 5, FEROMONERATE: 0.2}
        },
        INITIALPOINT: 'B', EDGES: {
                                    {INITIALPOINT: 'B', FINALPOINT: 'A', DISTANCE: 2, FEROMONERATE: 0.1},
                                    {INITIALPOINT: 'B', FINALPOINT: 'C', DISTANCE: 2, FEROMONERATE: 0.1},
                                    {INITIALPOINT: 'B', FINALPOINT: 'D', DISTANCE: 4, FEROMONERATE: 0.2},
                                    {INITIALPOINT: 'B', FINALPOINT: 'E', DISTANCE: 6, FEROMONERATE: 0.3}
        },
        INITIALPOINT: 'C', EDGES: {
                                    {INITIALPOINT: 'C', FINALPOINT: 'A', DISTANCE: 5, FEROMONERATE: 0.1},
                                    {INITIALPOINT: 'C', FINALPOINT: 'B', DISTANCE: 2, FEROMONERATE: 0.1},
                                    {INITIALPOINT: 'C', FINALPOINT: 'D', DISTANCE: 5, FEROMONERATE: 0.5},
                                    {INITIALPOINT: 'C', FINALPOINT: 'E', DISTANCE: 5, FEROMONERATE: 0.1}
        },
        INITIALPOINT: 'D', EDGES: {
                                    {INITIALPOINT: 'D', FINALPOINT: 'A', DISTANCE: 5, FEROMONERATE: 0.2},
                                    {INITIALPOINT: 'D', FINALPOINT: 'B', DISTANCE: 4, FEROMONERATE: 0.2},
                                    {INITIALPOINT: 'D', FINALPOINT: 'C', DISTANCE: 5, FEROMONERATE: 0.5},
                                    {INITIALPOINT: 'D', FINALPOINT: 'E', DISTANCE: 6, FEROMONERATE: 0.6}
        },
        INITIALPOINT: 'E', EDGES: {
                                    {INITIALPOINT: 'E', FINALPOINT: 'A', DISTANCE: 3, FEROMONERATE: 0.2},
                                    {INITIALPOINT: 'E', FINALPOINT: 'B', DISTANCE: 6, FEROMONERATE: 0.3},
                                    {INITIALPOINT: 'E', FINALPOINT: 'C', DISTANCE: 5, FEROMONERATE: 0.1},
                                    {INITIALPOINT: 'E', FINALPOINT: 'D', DISTANCE: 6, FEROMONERATE: 0.6}
        },
    }