import javax.swing.*;
import java.awt.*;
public class Main extends JPanel {
    public Main(){
        setPreferredSize(new Dimension(800,600));
        setBackground(Color.BLACK);
    }
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        // Draw the game here.
    }
    public static void main(String[] args){
        SwingUtilities.invokeLater(()->{
            JFrame window=new JFrame("Paws with Claws");
            window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            window.setContentPane(new Main());
            window.pack();
            window.setLocationRelativeTo(null);
            window.setVisible(true);
        });
    }
}