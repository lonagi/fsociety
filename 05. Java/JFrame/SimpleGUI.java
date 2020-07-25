package com.company;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class SimpleGUI extends JFrame {
    private JTextField a = new JTextField("ыы",10);
    private JLabel c = new JLabel("azaza");
    private JButton b = new JButton("Нажми на меня))");

    public SimpleGUI() {
        super("Test me");
        this.setBounds(500,500,500,500);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        Container co = this.getContentPane();
        co.setLayout(new GridLayout(3,5,2,2));

        JPanel rowPanel = new JPanel();
        rowPanel.add(c);
        rowPanel.add(a);
        co.add( rowPanel );

        co.add(b);


        b.addActionListener(new ButtonEventListener());
    }

    class ButtonEventListener implements ActionListener{
        public void actionPerformed(ActionEvent i){
            System.out.println("Lol button");

            JOptionPane.showMessageDialog(null,"lol","titile))",JOptionPane.PLAIN_MESSAGE);

        }
    }
}
