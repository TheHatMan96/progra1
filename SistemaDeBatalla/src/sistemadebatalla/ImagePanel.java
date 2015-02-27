package sistemadebatalla;
import java.awt.*;
import javax.swing.*;
/**
 *
 * @author elaprendiz - asumaretv http://www.youtube.com/user/JleoD7
 */
public class ImagePanel extends JPanel{

    private Image img;//almacenar para acceso facil
    public ImagePanel(Image img) {
        this.img = img;//referencia
        Dimension dimension = new Dimension(img.getWidth(null),img.getHeight(null));//estableccer dimessiones del panel
        this.setPreferredSize(dimension);
        this.setMaximumSize(dimension);
        this.setMaximumSize(dimension);
        this.setSize(dimension);
        this.setLayout(null);
    }

    @Override
    protected void paintComponent(Graphics g) {
        g.drawImage(img, 0, 0,null);
    }
    
    
    
    
}
