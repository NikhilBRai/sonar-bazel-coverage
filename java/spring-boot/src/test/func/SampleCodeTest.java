package func;

import com.bmuschko.SampleCode;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

//import static org.junit.jupiter.api.Assertions.assertEquals;

public class SampleCodeTest {


    @Test
    public void testingMethod() {
        //assertTrue(true);
        SampleCode s = new SampleCode();
        assertEquals(s.sampleMethod(), true);
    }
}