/*
 *
 */

#ifndef lcd_h_
#define lcd_h_

extern void send_text (char *str);
extern void set_reg_value8 (int reg, int val);
extern void clear(void);
extern void contrast(int cont);
extern void backlight(int light);
extern void write_text(int x, int y, char *text);

#endif
