import java.io.File;
import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;

public class ExistFile
{
	public static boolean isFileExist(String dir) {
		try {
			dir = URLDecoder.decode(dir, "UTF-8");
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
		}
		File f = new File(dir);
		if(f.exists() && !f.isDirectory())
			return true;
		return false;
	}
}
