tetromino t1 {
    type = T1;
    color = 5;
}

tetromino t2 {
    type = T2;
    color = 3;
}

control c1 {
    key = 3;
    action = 8;
}

control c2 {
    key = 2;
    action = 9;
}

gameboard gb1 {
    x_size = 32;
    y_size = 32;
    falling_speed = 2;
}

game g1 {
    board = gb1;
    levels = 15;
    controls = [c1, c2];
    blocks = [t1, t2];
}

main {
    play g1;
}