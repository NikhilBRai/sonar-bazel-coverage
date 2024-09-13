package func;

import com.bmuschko.SampleCode2;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class a {
    @Test
    public void testingMethod() {
        //assertTrue(true);
        SampleCode2 s = new SampleCode2();
        assertEquals(s.sampleMethod(), true);
    }
}
