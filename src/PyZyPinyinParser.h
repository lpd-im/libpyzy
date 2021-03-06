/* vim:set et ts=4 sts=4:
 *
 * libpyzy - The Chinese PinYin and Bopomofo conversion library.
 *
 * Copyright (c) 2008-2010 Peng Huang <shawn.p.huang@gmail.com>
 *
 * This library is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of the
 * License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
 * USA
 */
#ifndef __PYZY_PINYIN_PARSER_H_
#define __PYZY_PINYIN_PARSER_H_

#include <glib.h>
#include "PyZyString.h"
#include "PyZyPinyinArray.h"

namespace PyZy {

class PinyinParser {
public:
    static guint parse (const String &pinyin,      // pinyin string
                        gint          len,         // length of pinyin string
                        guint         option,      // option
                        PinyinArray  &result,      // store pinyin in result
                        guint         max);        // max length of the result
    static const Pinyin * isPinyin (gint sheng, gint yun, guint option);
    static guint parseBopomofo (const std::wstring  &bopomofo,
                                gint                 len,
                                guint                option,
                                PinyinArray         &result,
                                guint                max);
    static gboolean isBopomofoToneChar (const wchar_t ch);

};

};  // namespace PyZy

#endif  // __PYZY_PINYIN_PARSER_H_
