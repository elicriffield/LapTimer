/*
 * bw_lcd.c. 
 *
 * Control the BitWizard SPI-LCD expansion boards. 
 *
 * based on: 
 * SPI testing utility (using spidev driver)
 *
 * Copyright (c) 2007  MontaVista Software, Inc.
 * Copyright (c) 2007  Anton Vorontsov <avorontsov@ru.mvista.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; version 2 of the License.
 *
 * Cross-compile with cross-gcc -I/path/to/cross-kernel/include
 *
 *
 *
 * Compile on raspberry pi with 
 *
 * gcc -Wall -O2 bw_lcd.c -o bw_lcd 
 *
 */


#include <stdint.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <fcntl.h>
#include <string.h>
#include <sys/ioctl.h>
#include <linux/types.h>
#include <linux/spi/spidev.h>

#define ARRAY_SIZE(a) (sizeof(a) / sizeof((a)[0]))


static const char *device = "/dev/spidev0.0";
static uint8_t mode;
static uint8_t bits = 8;
static uint32_t speed = 450000;
static uint16_t delay = 2;
static int cls = 0;
static int reg = -1;
static int val = -1;
static int x = -1, y = -1, addr=0x82; 


static void pabort(const char *s)
{
  perror(s);
  abort();
}


static void transfer(int fd, int len, char *buf)
{
  int ret;
  uint8_t rx[0x80] = {0, };
  struct spi_ioc_transfer tr = {
    .tx_buf = 0,
    .rx_buf = (unsigned long)rx,
    .len = 0,
    .delay_usecs = delay,
    .speed_hz = speed,
    .bits_per_word = bits,
  };

  //printf("txbuf:%d, rxbuf:%d, len:%d, delay_usecs:%d, \n speed_hz:%d, bits_per_word:%d\n",(unsigned int)buf,len,0,delay,speed,bits);

  tr.tx_buf = (unsigned long)buf;	
  tr.len = len;
  ret = ioctl(fd, SPI_IOC_MESSAGE(1), &tr);
  if (ret < 1)
    pabort("can't send spi message\n");

#if 0
  for (ret = 0; ret < len ; ret++) {
    if (!(ret % 6))
      puts("");
    printf("%.2X \n", rx[ret]);
  }
  puts("");
#endif

}


static void send_text (char *str)
{
  int fd;
  char *buf;
  int l;
  fd = open_device();
  l = strlen (str);
  buf = malloc (l + 5); 
  buf[0] = addr;
  buf[1] = 0; 
  strcpy (buf+2, str); 
  transfer (fd, l+2, buf);
  free (buf);
  close(fd);
}

static void set_reg_value8 (int reg, int val)
{
  int fd;
  fd = open_device();
  //printf("set_reg_value8: reg:%d, val:%d\n",reg, val);
  char buf[5]; 
  buf[0] = addr;
  buf[1] = reg;
  buf[2] = val;
  transfer (fd, 3, buf);
  close(fd);
}

int open_device ()
{

  int ret = 0;
  int fd;
  char buf[0x100];
  int i;

  fd = open(device, O_RDWR);
  if (fd < 0)
    pabort("can't open device");

  /*
   * spi mode
   */
  ret = ioctl(fd, SPI_IOC_WR_MODE, &mode);
  if (ret == -1)
    pabort("can't set spi mode");

  ret = ioctl(fd, SPI_IOC_RD_MODE, &mode);
  if (ret == -1)
    pabort("can't get spi mode");

  /*
   * bits per word
   */
  ret = ioctl(fd, SPI_IOC_WR_BITS_PER_WORD, &bits);
  if (ret == -1)
    pabort("can't set bits per word");

  ret = ioctl(fd, SPI_IOC_RD_BITS_PER_WORD, &bits);
  if (ret == -1)
    pabort("can't get bits per word");

  /*
   * max speed hz
   */
  ret = ioctl(fd, SPI_IOC_WR_MAX_SPEED_HZ, &speed);
  if (ret == -1)
    pabort("can't set max speed hz");

  ret = ioctl(fd, SPI_IOC_RD_MAX_SPEED_HZ, &speed);
  if (ret == -1)
    pabort("can't get max speed hz");

  // printf("spi mode: %d\n", mode);
  // printf("bits per word: %d\n", bits);
  // printf("max speed: %d Hz (%d KHz)\n", speed, speed/1000);
  return fd;

}

void clear()
{
  set_reg_value8 (0x10, 0xaa);
}

void contrast(int cont)
{
  set_reg_value8 (0x12, cont);
}

void backlight(int light)
{
  set_reg_value8 (0x13, light);
}

void write_text(int x, int y, char *text)
{
  set_reg_value8 (0x11, (y << 5) | x);
  send_text (text);
}