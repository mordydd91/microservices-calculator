import java.awt.EventQueue;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import java.awt.Dimension;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.SwingConstants;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.io.File;
import java.util.ArrayList;
import java.awt.event.ActionEvent;
import java.awt.Font;

public class CalcGUI {

	private JFrame frame;
	private JTextField textField2;
	private JLabel lblOp;
	private JLabel lbl;
	private JLabel resultLablel;
	private JButton plusButton;
	private JButton minusButton;
	private JButton multButton;
	private JButton divButton;
	private JButton modButton;
	private JButton rootButton;
	private JTextField textField1;
	
	private String pythonPath = "python";
//	private static String basePath = new File(CalcGUI.class.getResource("").getFile()).getAbsolutePath();
	public static String pythonServicesPath = System.getProperty("user.dir") + "\\python";

	private String activateMicro(String name){
		ArrayList<String> arr = new ArrayList<>();
		try {
			float a = Float.parseFloat(textField1.getText());
			float b = Float.parseFloat(textField2.getText());
			arr.add(a+"");
			arr.add(b+"");
		}
		catch (Exception e) {
			JOptionPane.showMessageDialog(null, "Fields cannot be empty");
		}
		String path= "\"" +pythonServicesPath+"\\"+name+".py\"";
		String res = RunCmdService.runCmd(pythonPath, path, arr);
		return res;
	}

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		System.out.println();
		EventQueue.invokeLater(()->{
				try {
					CalcGUI window = new CalcGUI();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			});
	}

	/**
	 * Create the application.
	 */
	public CalcGUI() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
	    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setTitle("Calculator microservices");
		frame.setSize(new Dimension(701, 428));
		frame.getContentPane().setLayout(null);
		frame.setResizable(false);
		
		JLabel lblTitle = new JLabel("Calculator - Microservices");
		lblTitle.setVerticalAlignment(SwingConstants.TOP);
		lblTitle.setFont(new Font("Tahoma", Font.PLAIN, 30));
		lblTitle.setBounds(177, 11, 359, 52);
		frame.getContentPane().add(lblTitle);
		
		textField1 = new JTextField();
		textField1.setFont(new Font("Tahoma", Font.PLAIN, 20));
		textField1.setColumns(10);
		textField1.setBounds(66, 97, 112, 46);
		frame.getContentPane().add(textField1);
		
		textField2 = new JTextField();
		textField2.setFont(new Font("Tahoma", Font.PLAIN, 20));
		textField2.setBounds(278, 97, 112, 46);
		frame.getContentPane().add(textField2);
		textField2.setColumns(10);
		
		lblOp = new JLabel("OP");
		lblOp.setFont(new Font("Tahoma", Font.PLAIN, 20));
		lblOp.setBounds(213, 104, 55, 30);
		frame.getContentPane().add(lblOp);
		
		lbl = new JLabel("=");
		lbl.setFont(new Font("Tahoma", Font.PLAIN, 20));
		lbl.setBounds(419, 112, 36, 14);
		frame.getContentPane().add(lbl);
		
		resultLablel = new JLabel("RESULT");
		resultLablel.setFont(new Font("Tahoma", Font.PLAIN, 20));
		resultLablel.setBounds(481, 100, 208, 39);
		frame.getContentPane().add(resultLablel);
		
		plusButton = new JButton("+");
		plusButton.setFont(new Font("Tahoma", Font.PLAIN, 25));
		plusButton.addActionListener((e)->{UpdateResult.updateResult(activateMicro("plus"), resultLablel);});
		plusButton.setHorizontalAlignment(SwingConstants.LEFT);
		plusButton.setBounds(36, 259, 55, 52);
		frame.getContentPane().add(plusButton);
		
		minusButton = new JButton("-");
		minusButton.addActionListener((e)->{UpdateResult.updateResult(activateMicro("minus"), resultLablel);});
		minusButton.setHorizontalAlignment(SwingConstants.LEFT);
		minusButton.setFont(new Font("Tahoma", Font.PLAIN, 30));
		minusButton.setBounds(135, 259, 55, 52);
		frame.getContentPane().add(minusButton);
		
		multButton = new JButton("*");
		multButton.addActionListener((e)->{UpdateResult.updateResult(activateMicro("mult"), resultLablel);});
		multButton.setHorizontalAlignment(SwingConstants.LEFT);
		multButton.setFont(new Font("Tahoma", Font.PLAIN, 30));
		multButton.setBounds(232, 259, 55, 52);
		frame.getContentPane().add(multButton);
		
		divButton = new JButton("/");
		divButton.addActionListener((e)->{
			try {
				if(Float.parseFloat(textField2.getText())==0)
					PopoUpDivByZero.getPopUpMsgDivByZero();
				UpdateResult.updateResult(activateMicro("div"), resultLablel);
			}
			catch (Exception e1) {
				JOptionPane.showMessageDialog(null, "Fields cannot be empty");
			}
		});
		divButton.setHorizontalAlignment(SwingConstants.LEFT);
		divButton.setFont(new Font("Tahoma", Font.PLAIN, 30));
		divButton.setBounds(335, 259, 55, 52);
		frame.getContentPane().add(divButton);
		
		modButton = new JButton("%");
		modButton.setHorizontalAlignment(SwingConstants.LEFT);
		modButton.setFont(new Font("Tahoma", Font.PLAIN, 15));
		modButton.setBounds(435, 259, 55, 52);
		modButton.addActionListener((e)->{
			try {
				if(Float.parseFloat(textField2.getText())==0)
					PopoUpDivByZero.getPopUpMsgDivByZero();
				UpdateResult.updateResult(activateMicro("modulo"), resultLablel);
			}
			catch (Exception e2) {
				JOptionPane.showMessageDialog(null, "Fields cannot be empty");
			}
		});
		frame.getContentPane().add(modButton);
		
		rootButton = new JButton("Root");
		rootButton.setHorizontalAlignment(SwingConstants.LEFT);
		rootButton.setFont(new Font("Tahoma", Font.PLAIN, 30));
		rootButton.setToolTipText("The root of the function: x^2-2");
		rootButton.setBounds(533, 259, 108, 52);
		rootButton.addActionListener((e)->{
			String path= "\"" +pythonServicesPath+"\\"+"secant_method"+".py\"";
			if(ExistFile.isFileExist(path.substring(1, path.length()-1))) {
				String res = RunCmdService.runCmd(pythonPath, path, new ArrayList<String>());
				resultLablel.setText(res + " By secant");
			}
			else {
				path= "\"" +pythonServicesPath+"\\"+"bisection_method"+".py\"";
				if(ExistFile.isFileExist(path.substring(1, path.length()-1))) {
					String res = RunCmdService.runCmd(pythonPath, path, new ArrayList<String>());
					resultLablel.setText(res + " By bisection");
				}
				else
					JOptionPane.showMessageDialog(null, "Cannot find microservice");
			}
		});
		frame.getContentPane().add(rootButton);
	}
}
