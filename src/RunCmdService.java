import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URLDecoder;
import java.util.ArrayList;

public class RunCmdService {
			
	public static String runCmd(String pythonPath, String filePath, ArrayList<String> args) {
		String a = "";
		for(String s:args) {a+=s+" ";}
		String path = pythonPath + " " + filePath + " " + a;
		String decoded = null;
		try {
			decoded = URLDecoder.decode(path, "UTF-8");
		}
		catch (Exception e) {}
		return new RunCmdService().executeCommand(decoded);
	}
	
	private String executeCommand(String command) {

		StringBuffer output = new StringBuffer();

		Process p;
		try {
			p = Runtime.getRuntime().exec(command);
			p.waitFor();
			BufferedReader reader = 
                            new BufferedReader(new InputStreamReader(p.getInputStream()));
			String line = "";			
			while ((line = reader.readLine())!= null) {
				output.append(line + "\n");
			}

		} catch (Exception e) {
			e.printStackTrace();
		}
		return output.toString();

	}
}
