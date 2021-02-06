package com.hosticlefifer.lsm_control;

import javax.swing.*;

/**
 * A class to display errors in dialogs.
 */
public class ErrorDisplay {
    public static void alert(String problem, Exception e) {
        JOptionPane.showMessageDialog(JOptionPane.getRootFrame(), problem + "\n" + e, "Error", JOptionPane.ERROR_MESSAGE);
    }
}
