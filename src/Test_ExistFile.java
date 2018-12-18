import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.Test;

public class Test_ExistFile
{
	@Test
	public void test_ifExistFile() {
        assertEquals(false, ExistFile.isFileExist("Null dir"));
        assertEquals(false, ExistFile.isFileExist(""));
        assertEquals(false, ExistFile.isFileExist(""));
    }
}
