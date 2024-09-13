package func;

import com.bmuschko.SampleCode;
import com.bmuschko.SampleCode2;
import com.bmuschko.SampleCode3;
import com.bmuschko.SampleCode4;
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

    @Test
    public void testingMethod2() {
        //assertTrue(true);
        SampleCode2 s = new SampleCode2();
        assertEquals(s.sampleMethod(), true);
    }

    @Test
    public void testingMethod3() {
        //assertTrue(true);
        SampleCode3 s = new SampleCode3();
        assertEquals(s.sampleMethod(), true);
    }

    @Test
    public void testingMethod4() {
        //assertTrue(true);
        SampleCode4 s = new SampleCode4();
        assertEquals(s.sampleMethod(), true);
    }
}