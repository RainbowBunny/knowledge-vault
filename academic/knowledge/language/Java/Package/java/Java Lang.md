# Parent: Object
## Math

Constant: `E`, `PI`.
**Instance Method**:

| Method      | Parameter                          | Note                                                 |
| ----------- | ---------------------------------- | ---------------------------------------------------- |
| `abs`       |                                    |                                                      |
| `ceil`      | `double d`                         |                                                      |
| `floor`     | `double d`                         |                                                      |
| `rint`      | `double d`                         |                                                      |
| `round`     |                                    |                                                      |
| `min`       |                                    |                                                      |
| `max`       |                                    |                                                      |
| `exp`       | `double d`                         |                                                      |
| `log`       | `double d`                         |                                                      |
| `pow`       | `double base`<br>`double exponent` |                                                      |
| `sqrt`      | `double d`                         |                                                      |
| `sin`       | `double d`                         |                                                      |
| `cos`       | `double d`                         |                                                      |
| `tan`       | `double d`                         |                                                      |
| `asin`      | `double d`                         |                                                      |
| `acos`      | `double d`                         |                                                      |
| `atan`      | `double d`                         |                                                      |
| `atan2`     | `double y`<br>`double x`           | Convert `(x, y)` to `(r, theta)` and returns `theta` |
| `toDegree`  | `double d`                         |                                                      |
| `toRadians` | `double d`                         |                                                      |
| `random`    |                                    | Random `double` in range `[0, 1)`.                   |

## Character

**Class Method**: `isLetter`, `isDigit`, `isWhitespace`, `isUpperCase`, `isLowerCase`, `toUpperCase`, `toLowerCase`

## Number

**Instance Method**: `byteValue`, `shortValue`, `intValue`, `longValue`, `floatValue`, `DoubleValue`

**Class Method**:

| Method     | Parameter                   | Return    | Note |
| ---------- | --------------------------- | --------- | ---- |
| `decode`   | `String s`                  | `Integer` |      |
| `parseInt` | `String s`<br>`[int radix]` | `int`     |      |
| `valueOf`  | `int i`                     | `Integer` |      |
| `valueOf`  | `String s`<br>`[int radix]` | `Integer` |      |

## String

**Instance Method**:

| Method        | Parameter                                                                                |
| ------------- | ---------------------------------------------------------------------------------------- |
| `copyValueOf` | `char[] data`<br>`[int offset]`<br>`[int count]`                                         |
| `format`      | `[Locale l]`<br>`String format`<br>`Object... args`                                      |
| `join`        | `CharSequence delimiter`<br>`Iterable<? extends CharSequence>\|CharSequence... elements` |
| `valueOf`     |                                                                                          |

**Class Method**:

| Method                         | Parameter                                                                               | Return         | Note                                                                |
| ------------------------------ | --------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------- |
| `charAt`                       | `int index`                                                                             | `char`         |                                                                     |
| `concat`                       | `String str`                                                                            | `String`       |                                                                     |
| `substring`                    | `int beginIndex`<br>`[int endIndex]`                                                    | `String`       |                                                                     |
| `split`                        | `String regex`<br>`[int limit]`                                                         | `String[]`     |                                                                     |
| `subSequence`                  | `int beginIndex`<br>`int endIndex`                                                      | `CharSequence` |                                                                     |
| `trim`                         |                                                                                         | `String`       | Remove leading and trailing white space                             |
| `toLowerCase`<br>`toUpperCase` |                                                                                         | `String`       |                                                                     |
| `indexOf`<br>`lastIndexOf`     | `int ch \| String str`<br>`[int fromIndex]`                                             | `int`          | Index of first/last character and string                            |
| `contains`                     | `CharSequence`                                                                          | `boolean`      |                                                                     |
| `replace`                      | `char oldChar`<br>`char newChar`                                                        | `String`       |                                                                     |
| `replace`                      | `CharSequence target`<br>`CharSequence replacement`                                     | `String`       |                                                                     |
| `replaceAll`                   | `String regex`<br>`String replacement`                                                  | `String`       |                                                                     |
| `replaceFirst`                 | `String regex`<br>`String replacement`                                                  | `String`       |                                                                     |
| `endsWith`                     | `String suffix`                                                                         | `boolean`      |                                                                     |
| `startsWith`                   | `String prefix`<br>`[int offset]`                                                       | `boolean`      |                                                                     |
| `compareToIgnoreCase`          | `String str`                                                                            | `int`          |                                                                     |
| `regionMatches`                | `[boolean ignoreCase]`<br>`int toffset`<br>`String other`<br>`int ooffset`<br>`int len` | `boolean`      | Compare:<br>`this[toofset]`<br>`other[ooffset]`<br>For length `len` |
| `matches`                      | `String regex`                                                                          | `boolean`      |                                                                     |

## StringBuilder

**Constructor**:
- No parameter
- `CharSequence cs`
- `int initCapacity`
- `String s`
**Instance Method**:

| Method         | Parameter                                                | Return          | Note                                                                  |
| -------------- | -------------------------------------------------------- | --------------- | --------------------------------------------------------------------- |
| `append`       | `Object obj`                                             | `StringBuilder` |                                                                       |
| `delete`       | `int start`<br>`int end`                                 | `StringBuilder` |                                                                       |
| `deleteCharAt` | `int index`                                              | `StringBuilder` |                                                                       |
| `insert`       | `int offset`<br>`Object obj`                             | `StringBuilder` |                                                                       |
| `insert`       | `int index`<br>`char[] str`<br>`int offset`<br>`int len` | `StringBuilder` | `index` – Position of original string<br>`offset` – Position of `str` |
| `replace`      | `int start`<br>`int end`<br>`String s`                   | `StringBuilder` |                                                                       |
| `setCharAt`    | `int index`<br>`char c`                                  |                 |                                                                       |
| `reverse`      |                                                          | `StringBuilder` |                                                                       |


# Parent: Number
## Byte


## Double


## Float


## Integer


## Long


## Short


