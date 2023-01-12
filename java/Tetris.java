import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class Tetris extends JFrame {
    private Cell[][] cells;
    private Tetromino tetromino;

    private Tetris() {
        setTitle("Tetris");
        setSize(Settings.Size * 10 + Settings.BORDER * 11 + 6, Settings.Size * 20 + Settings.BORDER * 21 + 29);
        setResizable(false);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        init();

        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                switch (e.getKeyCode()) {
                    case KeyEvent.VK_W:
                    case KeyEvent.VK_K:
                        tetromino.clockwise();
                        if (over())
                            for (int i = 0; i < 3; i++)
                                tetromino.clockwise();
                        break;
                    case KeyEvent.VK_J:
                        for (int i = 0; i < 3; i++)
                            tetromino.clockwise();
                        if (over())
                            tetromino.clockwise();
                        break;
                    case KeyEvent.VK_A:
                        tetromino.move(-1, 0);
                        if (over())
                            tetromino.move(1, 0);
                        break;
                    case KeyEvent.VK_D:
                        tetromino.move(1, 0);
                        if (over())
                            tetromino.move(-1, 0);
                        break;
                    case KeyEvent.VK_S:
                        tetromino.move(0, 1);
                        if (over())
                            downOver();
                        break;
                    case KeyEvent.VK_SPACE:
                        while (!over())
                            tetromino.move(0, 1);
                        downOver();
                        break;
                    case KeyEvent.VK_R:
                        init();
                        break;
                }
                repaint();
            }
        });

        new Thread(() -> {
            while (true) {
                try {
                    Thread.sleep(Settings.SPEED);
                    tetromino.move(0, 1);
                    if (over())
                        downOver();
                    repaint();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }

    private void init() {
        Settings.randomBlockColor();
        cells = new Cell[20][10];
        for (int i = 0; i < 20; i++)
            for (int j = 0; j < 10; j++)
                cells[i][j] = new Cell(i, j, null);
        tetromino = new Tetromino();
    }

    @Override
    public void paint(Graphics g) {
        int size = Settings.Size + Settings.BORDER;
        Image image = createImage(getWidth(), getHeight());
        Graphics2D g2 = (Graphics2D) image.getGraphics();

        g2.setStroke(new BasicStroke(Settings.BORDER));

        g2.setColor(Settings.BORDER_COLOR);
        for (int i = 0; i < 20; i++)
            for (int j = 0; j < 10; j++)
                g2.drawRect(j * size + Settings.BORDER / 2, i * size + Settings.BORDER / 2, size, size);

        for (int i = 0; i < 20; i++)
            for (int j = 0; j < 10; j++) {
                g2.setColor(cells[i][j].getColor() == null ? Settings.BACKGROUND_COLOR : cells[i][j].getColor());
                g2.fillRect(j * size + Settings.BORDER, i * size + Settings.BORDER, Settings.Size, Settings.Size);
            }

        for (int i = 0; i < 4; i++) {
            g2.setColor(tetromino.getCell()[i].getColor());
            g2.fillRect(tetromino.getCell()[i].getY() * size + Settings.BORDER, tetromino.getCell()[i].getX() * size + Settings.BORDER, Settings.Size, Settings.Size);
        }

        g.drawImage(image, 3, 26, null);
    }

    private boolean over() {
        for (int i = 0; i < 4; i++)
            if (tetromino.getCell()[i].getY() < 0 || tetromino.getCell()[i].getY() > 9 || tetromino.getCell()[i].getX() > 19 || tetromino.getCell()[i].getX() >= 0 && cells[tetromino.getCell()[i].getX()][tetromino.getCell()[i].getY()].getColor() != null)
                return true;
        return false;
    }

    private void downOver() {
        tetromino.move(0, -1);
        for (int i = 0; i < 4; i++)
            cells[tetromino.getCell()[i].getX()][tetromino.getCell()[i].getY()].setColor(tetromino.getCell()[i].getColor());

        tetromino = new Tetromino();
        for (int i = 0; i < 4; i++)
            if (cells[tetromino.getCell()[i].getX()][tetromino.getCell()[i].getY()].getColor() != null) {
                repaint();
                try {
                    Thread.sleep(Settings.SPEED);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                init();
            }

        boolean clear;
        for (int i = 0; i < 20; i++) {
            clear = true;
            for (int j = 0; j < 10; j++) {
                if (cells[i][j].getColor() == null) {
                    clear = false;
                    break;
                }
            }
            if (clear)
                for (int i1 = i; i1 >= 0; i1--)
                    for (int j = 0; j < 10; j++)
                        cells[i1][j].setColor(i1 != 0 ? cells[i1 - 1][j].getColor() : null);
        }
    }

    public static void main(String[] args) {
        new Tetris().setVisible(true);
    }
}
