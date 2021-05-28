package com.hosticlefifer.lsm_control.pattern_script;

import com.hosticlefifer.lsm_control.Commands.Command;

import java.util.ArrayList;
import java.util.HashMap;

/**
 * Parser for pattern script
 * Example script:
 * ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 * + set a                       ; a = 0;
 * + set b
 * + set c
 * + for 0 to 100 by 5 as a      ; for(int a=0; a<=100; a+=5)
 * +   for 0 to 100 by 3 as b    ;         b
 * +     for 10 to 20 by 1 as c  ;         c
 * +       increment a by 1      ; a += 1;
 * +       decrement a by 1      ; a -= 1;
 * +       pixel (a,b,c)         ; goto position a,b,c
 * +       set a to 10           ; a = 10;
 * +     rof
 * +   rof
 * + rof
 * + end
 * ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 *   
 * The variables a-z may be used, as long as they are initialized first
 * Statements are executed line by line.
 */
public class Parser {
    private final HashMap<String, Integer> variables = new HashMap<>();
    private final String[] lines;
    private ArrayList<Command> commands;

    public Parser(String code) {
        lines = code.split("\n?\r");
    }

    public int execute() throws PatternScriptException {
        return execute(0);
    }

    private int execute(int startLine) throws PatternScriptException {
        commands = new ArrayList<>();
        int num = 0;  // line number
        for(num = startLine; num < lines.length; num++) {
            if (lines[num] == null || lines[num].length() < 1) continue;
            // Process command:
            if(lines[num].contains("rof") || lines[num].contains("end")) {
                return num;
            } else if(lines[num].contains("set")) {
                setVariable(stringAfter(lines[num], "set"), valueAfter(lines[num], "to"));
            } else if(lines[num].contains("increment")) {
                setVariable(stringAfter(lines[num], "increment"), valueAfter(lines[num], "increment") + valueAfter(lines[num], "by"));
            } else if(lines[num].contains("decrement")) {
                setVariable(stringAfter(lines[num], "decrement"), valueAfter(lines[num], "decrement") - valueAfter(lines[num], "by"));
            } else if(lines[num].contains("print")) {
                System.out.println(valueAfter(lines[num], "print"));
            } else if(lines[num].contains("for")) {
                int init = valueAfter(lines[num], "for");
                int stop = valueAfter(lines[num], "to");
                int step = valueAfter(lines[num], "by");
                String var = stringAfter(lines[num], "as");
                int linesPassed = 0;
                if(step > 0) {
                    for(int count = init; count <= stop; count += step) {
                        setVariable(var, count);
                        linesPassed = execute(num);
                    }
                } else {
                    for(int count = init; count >= stop; count += step) {
                        setVariable(var, count);
                        linesPassed = execute(num);
                    }
                }
                num += linesPassed;
            } else if(lines[num].contains("pixel")) {
                String[] orderedPair = (lines[num].substring(lines[num].indexOf('(')))  // (x, y, z)
                        .replaceAll("[^0-9A-Za-z,]", "")               // x,y,z
                        .split(",");                                              // ["x", "y", "z"]
                System.out.println(orderedPair);
            }
        }
        return num;
    }

    private Integer valueAfter(String line, String key) throws PatternScriptException {
        return getValue(stringAfter(line, key));
    }

    private String stringAfter(String line, String key) {
        String chunk = line.substring(line.indexOf(key) + key.length());
        StringBuilder result = new StringBuilder();
        boolean passedLeadingSpaces = false;
        for(int i = 0; i < chunk.length(); i++) {
            if(!isAlphaNumeric(chunk.charAt(i))) {
                if(passedLeadingSpaces) break;
                continue;
            }
            passedLeadingSpaces = true;
            result.append(chunk.charAt(i));
        }
        return result.toString();
    }

    private static boolean isAlphaNumeric(char c) {
        return Character.isAlphabetic(c) || Character.isDigit(c);
    }

    private Integer getValue(String name) throws PatternScriptException {
        Integer var = getVariable(name);
        if(var == null && Character.isDigit(name.charAt(0))) {
            try {
                return Integer.parseInt(name);
            } catch(NumberFormatException e) {
                throw new PatternScriptException("Invalid constant " + name);
            }
        }
        return var;
    }

    private Integer getVariable(String name) {
        return variables.get(name);
    }

    private void setVariable(String name, int val) {
        variables.put(name, val);
    }

    public ArrayList<Command> getCommands() {
        return commands;
    }

    public static void main(String[] args) throws PatternScriptException {
        Parser parser = new Parser("set myVar to 1\n" +
                "increment myVar by 20\n" +
                "print myVar\n");
        System.out.println(parser.execute());
    }
}
