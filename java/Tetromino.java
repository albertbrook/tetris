import java.util.Random;

public class Tetromino {
    private Cell[][] cells = new Cell[4][4];
    private int state = 0;

    public Cell[] getCell() {
        return cells[state];
    }

    public Tetromino() {
        switch (new Random().nextInt(7)) {
            case 0:
                // O
                cells[0] = new Cell[]{
                        new Cell(0, 4, Settings.O_COLOR),
                        new Cell(0, 5, Settings.O_COLOR),
                        new Cell(1, 4, Settings.O_COLOR),
                        new Cell(1, 5, Settings.O_COLOR),
                };
                break;
            case 1:
                // I
                cells[0] = new Cell[]{
                        new Cell(0, 3, Settings.I_COLOR),
                        new Cell(0, 4, Settings.I_COLOR),
                        new Cell(0, 5, Settings.I_COLOR),
                        new Cell(0, 6, Settings.I_COLOR),
                };
                cells[1] = new Cell[]{
                        new Cell(-2, 5, Settings.I_COLOR),
                        new Cell(-1, 5, Settings.I_COLOR),
                        new Cell(0, 5, Settings.I_COLOR),
                        new Cell(1, 5, Settings.I_COLOR),
                };
                break;
            case 2:
                // T
                cells[0] = new Cell[]{
                        new Cell(0, 4, Settings.T_COLOR),
                        new Cell(0, 5, Settings.T_COLOR),
                        new Cell(0, 6, Settings.T_COLOR),
                        new Cell(1, 5, Settings.T_COLOR),
                };
                cells[1] = new Cell[]{
                        new Cell(-1, 5, Settings.T_COLOR),
                        new Cell(0, 4, Settings.T_COLOR),
                        new Cell(0, 5, Settings.T_COLOR),
                        new Cell(1, 5, Settings.T_COLOR),
                };
                cells[2] = new Cell[]{
                        new Cell(-1, 5, Settings.T_COLOR),
                        new Cell(0, 4, Settings.T_COLOR),
                        new Cell(0, 5, Settings.T_COLOR),
                        new Cell(0, 6, Settings.T_COLOR),
                };
                cells[3] = new Cell[]{
                        new Cell(-1, 5, Settings.T_COLOR),
                        new Cell(0, 5, Settings.T_COLOR),
                        new Cell(0, 6, Settings.T_COLOR),
                        new Cell(1, 5, Settings.T_COLOR),
                };
                break;
            case 3:
                // Z
                cells[0] = new Cell[]{
                        new Cell(0, 4, Settings.Z_COLOR),
                        new Cell(0, 5, Settings.Z_COLOR),
                        new Cell(1, 5, Settings.Z_COLOR),
                        new Cell(1, 6, Settings.Z_COLOR),
                };
                cells[1] = new Cell[]{
                        new Cell(-1, 6, Settings.Z_COLOR),
                        new Cell(0, 5, Settings.Z_COLOR),
                        new Cell(0, 6, Settings.Z_COLOR),
                        new Cell(1, 5, Settings.Z_COLOR),
                };
                break;
            case 4:
                // S
                cells[0] = new Cell[]{
                        new Cell(0, 5, Settings.S_COLOR),
                        new Cell(0, 6, Settings.S_COLOR),
                        new Cell(1, 4, Settings.S_COLOR),
                        new Cell(1, 5, Settings.S_COLOR),
                };
                cells[1] = new Cell[]{
                        new Cell(-1, 5, Settings.S_COLOR),
                        new Cell(0, 5, Settings.S_COLOR),
                        new Cell(0, 6, Settings.S_COLOR),
                        new Cell(1, 6, Settings.S_COLOR),
                };
                break;
            case 5:
                // L
                cells[0] = new Cell[]{
                        new Cell(0, 4, Settings.L_COLOR),
                        new Cell(0, 5, Settings.L_COLOR),
                        new Cell(0, 6, Settings.L_COLOR),
                        new Cell(1, 4, Settings.L_COLOR),
                };
                cells[1] = new Cell[]{
                        new Cell(-1, 4, Settings.L_COLOR),
                        new Cell(-1, 5, Settings.L_COLOR),
                        new Cell(0, 5, Settings.L_COLOR),
                        new Cell(1, 5, Settings.L_COLOR),
                };
                cells[2] = new Cell[]{
                        new Cell(-1, 6, Settings.L_COLOR),
                        new Cell(0, 4, Settings.L_COLOR),
                        new Cell(0, 5, Settings.L_COLOR),
                        new Cell(0, 6, Settings.L_COLOR),
                };
                cells[3] = new Cell[]{
                        new Cell(-1, 5, Settings.L_COLOR),
                        new Cell(0, 5, Settings.L_COLOR),
                        new Cell(1, 5, Settings.L_COLOR),
                        new Cell(1, 6, Settings.L_COLOR),
                };
                break;
            case 6:
                // J
                cells[0] = new Cell[]{
                        new Cell(0, 4, Settings.J_COLOR),
                        new Cell(0, 5, Settings.J_COLOR),
                        new Cell(0, 6, Settings.J_COLOR),
                        new Cell(1, 6, Settings.J_COLOR),
                };
                cells[1] = new Cell[]{
                        new Cell(-1, 5, Settings.J_COLOR),
                        new Cell(0, 5, Settings.J_COLOR),
                        new Cell(1, 4, Settings.J_COLOR),
                        new Cell(1, 5, Settings.J_COLOR),
                };
                cells[2] = new Cell[]{
                        new Cell(-1, 4, Settings.J_COLOR),
                        new Cell(0, 4, Settings.J_COLOR),
                        new Cell(0, 5, Settings.J_COLOR),
                        new Cell(0, 6, Settings.J_COLOR),
                };
                cells[3] = new Cell[]{
                        new Cell(-1, 5, Settings.J_COLOR),
                        new Cell(-1, 6, Settings.J_COLOR),
                        new Cell(0, 5, Settings.J_COLOR),
                        new Cell(1, 5, Settings.J_COLOR),
                };
                break;
        }
    }

    public void clockwise() {
        state++;
        if (state > 3 || cells[state][0] == null)
            state = 0;
    }

    public void move(int x, int y) {
        for (int i = 0; i < 4; i++) {
            if (cells[i][0] == null)
                break;
            for (int j = 0; j < 4; j++) {
                cells[i][j].setX(cells[i][j].getX() + y);
                cells[i][j].setY(cells[i][j].getY() + x);
            }
        }
    }
}
