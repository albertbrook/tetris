import java.awt.*;
import java.util.Random;

public class Settings {
    public static final int Size = 40;
    public static final int BORDER = 3;
    public static final int SPEED = 500;

    public static final Color BACKGROUND_COLOR = new Color(0, 0, 0);
    public static final Color BORDER_COLOR = new Color(127, 127, 127);

    public static Color O_COLOR;
    public static Color I_COLOR;
    public static Color T_COLOR;
    public static Color Z_COLOR;
    public static Color S_COLOR;
    public static Color L_COLOR;
    public static Color J_COLOR;

    static {
        randomBlockColor();
    }

    public static void randomBlockColor() {
        O_COLOR = randomColor();
        I_COLOR = randomColor();
        T_COLOR = randomColor();
        Z_COLOR = randomColor();
        S_COLOR = randomColor();
        L_COLOR = randomColor();
        J_COLOR = randomColor();
    }

    private static Color randomColor() {
        Random random = new Random();
        return new Color(random.nextInt(256), random.nextInt(256), random.nextInt(256));
    }
}
