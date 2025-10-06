package com.example;

import org.junit.Test;
import static org.junit.Assert.*;

public class AppTest {

    public static int counter = 0;
    public static int counter2 = 0;

    @Test
    public void add_twoNumbers_returnsSum() {
        assertEquals(7, App.add(3, 4));
    }

    @Test
    public void TestA() {
        assertEquals(0, counter);
    }

    @Test
    public void TestB() {
        counter = 42;
    }

    @Test
    public void TestC() {
        assertEquals(0, counter2);
    }

    @Test
    public void TestD() {
        counter2 = 42;
    }

    @Test
    public void add_handlesNegatives() {
        assertEquals(-1, App.add(2, -3));
        assertEquals(-5, App.add(-2, -3));
        assertEquals(0, App.add(0, 0));
    }
}