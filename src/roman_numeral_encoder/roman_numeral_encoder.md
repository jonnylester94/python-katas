# roman_numeral_encoder

The challenge is to implement a function which return a Roman Numeral string when passed a number of seconds.

If you're unfamiliar with Roman Numerals we have include a table showing at the bottom of this file.

## Examples

```py
roman_numeral_encoder(1)
# "I"
```

```py
roman_numeral_encoder(2)
# "II"
```

```py
roman_numeral_encoder(10)
# "X"
```

```py
roman_numeral_encoder(17)
# "XVII"
```

```py
roman_numeral_encoder(60)
# "LX"
```

```py
roman_numeral_encoder(75)
# "LXXV"
```

```py
roman_numeral_encoder(91)
# "XCI"
```

---

### Roman Numeral Table

<table>

<tbody><tr><td class="alternate"><b>	1	</b></td><td>	I	</td><td class="alternate"><b>	21	</b></td><td>	XXI	</td><td class="alternate"><b>	41	</b></td><td>	XLI	</td><td class="alternate"><b>	61	</b></td><td>	LXI	</td><td class="alternate"><b>	81	</b></td><td>	LXXXI	</td></tr>
<tr><td class="alternate"><b>	2	</b></td><td>	II	</td><td class="alternate"><b>	22	</b></td><td>	XXII	</td><td class="alternate"><b>	42	</b></td><td>	XLII	</td><td class="alternate"><b>	62	</b></td><td>	LXII	</td><td class="alternate"><b>	82	</b></td><td>	LXXXII	</td></tr>
<tr><td class="alternate"><b>	3	</b></td><td>	III	</td><td class="alternate"><b>	23	</b></td><td>	XXIII	</td><td class="alternate"><b>	43	</b></td><td>	XLIII	</td><td class="alternate"><b>	63	</b></td><td>	LXIII	</td><td class="alternate"><b>	83	</b></td><td>	LXXXIII	</td></tr>
<tr><td class="alternate"><b>	4	</b></td><td>	IV	</td><td class="alternate"><b>	24	</b></td><td>	XXIV	</td><td class="alternate"><b>	44	</b></td><td>	XLIV	</td><td class="alternate"><b>	64	</b></td><td>	LXIV	</td><td class="alternate"><b>	84	</b></td><td>	LXXXIV	</td></tr>
<tr><td class="alternate"><b>	5	</b></td><td>	V	</td><td class="alternate"><b>	25	</b></td><td>	XXV	</td><td class="alternate"><b>	45	</b></td><td>	XLV	</td><td class="alternate"><b>	65	</b></td><td>	LXV	</td><td class="alternate"><b>	85	</b></td><td>	LXXXV	</td></tr>
<tr><td class="alternate"><b>	6	</b></td><td>	VI	</td><td class="alternate"><b>	26	</b></td><td>	XXVI	</td><td class="alternate"><b>	46	</b></td><td>	XLVI	</td><td class="alternate"><b>	66	</b></td><td>	LXVI	</td><td class="alternate"><b>	86	</b></td><td>	LXXXVI	</td></tr>
<tr><td class="alternate"><b>	7	</b></td><td>	VII	</td><td class="alternate"><b>	27	</b></td><td>	XXVII	</td><td class="alternate"><b>	47	</b></td><td>	XLVII	</td><td class="alternate"><b>	67	</b></td><td>	LXVII	</td><td class="alternate"><b>	87	</b></td><td>	LXXXVII	</td></tr>
<tr><td class="alternate"><b>	8	</b></td><td>	VIII	</td><td class="alternate"><b>	28	</b></td><td>	XXVIII	</td><td class="alternate"><b>	48	</b></td><td>	XLVIII	</td><td class="alternate"><b>	68	</b></td><td>	LXVIII	</td><td class="alternate"><b>	88	</b></td><td>	LXXXVIII	</td></tr>
<tr><td class="alternate"><b>	9	</b></td><td>	IX	</td><td class="alternate"><b>	29	</b></td><td>	XXIX	</td><td class="alternate"><b>	49	</b></td><td>	XLIX	</td><td class="alternate"><b>	69	</b></td><td>	LXIX	</td><td class="alternate"><b>	89	</b></td><td>	LXXXIX	</td></tr>
<tr><td class="alternate"><b>	10	</b></td><td>	X	</td><td class="alternate"><b>	30	</b></td><td>	XXX	</td><td class="alternate"><b>	50	</b></td><td>	L	</td><td class="alternate"><b>	70	</b></td><td>	LXX	</td><td class="alternate"><b>	90	</b></td><td>	XC	</td></tr>
<tr><td class="alternate"><b>	11	</b></td><td>	XI	</td><td class="alternate"><b>	31	</b></td><td>	XXXI	</td><td class="alternate"><b>	51	</b></td><td>	LI	</td><td class="alternate"><b>	71	</b></td><td>	LXXI	</td><td class="alternate"><b>	91	</b></td><td>	XCI	</td></tr>
<tr><td class="alternate"><b>	12	</b></td><td>	XII	</td><td class="alternate"><b>	32	</b></td><td>	XXXII	</td><td class="alternate"><b>	52	</b></td><td>	LII	</td><td class="alternate"><b>	72	</b></td><td>	LXXII	</td><td class="alternate"><b>	92	</b></td><td>	XCII	</td></tr>
<tr><td class="alternate"><b>	13	</b></td><td>	XIII	</td><td class="alternate"><b>	33	</b></td><td>	XXXIII	</td><td class="alternate"><b>	53	</b></td><td>	LIII	</td><td class="alternate"><b>	73	</b></td><td>	LXXIII	</td><td class="alternate"><b>	93	</b></td><td>	XCIII	</td></tr>
<tr><td class="alternate"><b>	14	</b></td><td>	XIV	</td><td class="alternate"><b>	34	</b></td><td>	XXXIV	</td><td class="alternate"><b>	54	</b></td><td>	LIV	</td><td class="alternate"><b>	74	</b></td><td>	LXXIV	</td><td class="alternate"><b>	94	</b></td><td>	XCIV	</td></tr>
<tr><td class="alternate"><b>	15	</b></td><td>	XV	</td><td class="alternate"><b>	35	</b></td><td>	XXXV	</td><td class="alternate"><b>	55	</b></td><td>	LV	</td><td class="alternate"><b>	75	</b></td><td>	LXXV	</td><td class="alternate"><b>	95	</b></td><td>	XCV	</td></tr>
<tr><td class="alternate"><b>	16	</b></td><td>	XVI	</td><td class="alternate"><b>	36	</b></td><td>	XXXVI	</td><td class="alternate"><b>	56	</b></td><td>	LVI	</td><td class="alternate"><b>	76	</b></td><td>	LXXVI	</td><td class="alternate"><b>	96	</b></td><td>	XCVI	</td></tr>
<tr><td class="alternate"><b>	17	</b></td><td>	XVII	</td><td class="alternate"><b>	37	</b></td><td>	XXXVII	</td><td class="alternate"><b>	57	</b></td><td>	LVII	</td><td class="alternate"><b>	77	</b></td><td>	LXXVII	</td><td class="alternate"><b>	97	</b></td><td>	XCVII	</td></tr>
<tr><td class="alternate"><b>	18	</b></td><td>	XVIII	</td><td class="alternate"><b>	38	</b></td><td>	XXXVIII	</td><td class="alternate"><b>	58	</b></td><td>	LVIII	</td><td class="alternate"><b>	78	</b></td><td>	LXXVIII	</td><td class="alternate"><b>	98	</b></td><td>	XCVIII	</td></tr>
<tr><td class="alternate"><b>	19	</b></td><td>	XIX	</td><td class="alternate"><b>	39	</b></td><td>	XXXIX	</td><td class="alternate"><b>	59	</b></td><td>	LIX	</td><td class="alternate"><b>	79	</b></td><td>	LXXIX	</td><td class="alternate"><b>	99	</b></td><td>	XCIX	</td></tr>
<tr><td class="alternate"><b>	20	</b></td><td>	XX	</td><td class="alternate"><b>	40	</b></td><td>	XL	</td><td class="alternate"><b>	60	</b></td><td>	LX	</td><td class="alternate"><b>	80	</b></td><td>	LXXX	</td><td class="alternate"><b>	100	</b></td><td>	C	</td></tr></tbody></table>
