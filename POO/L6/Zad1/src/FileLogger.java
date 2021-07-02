import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class FileLogger implements ILogger {
    private String path ;

    public FileLogger(String path) {
        this.path = path;
    }

    public FileLogger() {
        path = "";
    }

    @Override
    public void Log(String message) {
        try(FileWriter fileWriter = new FileWriter(path);
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter)
                )
        {
            bufferedWriter.write(message);
            bufferedWriter.newLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
