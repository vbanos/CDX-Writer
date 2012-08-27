#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import commands
from pipes import quote

warcs = {'alexa_short_header.arc.gz':      'net,killerjo)/robots.txt 20110804181142 http://www.killerjo.net:80/robots.txt unk - YZI2NMZ5ILYICUL3PNYVYQR3KI2YY5EH - - 139 161 alexa_short_header.arc.gz',
         'bad_mime_type.arc.gz':           'net,naver,cafethumb)/20101223_84/qkrgns3_129303386816936xuq_jpg/imag0030_qkrgns3.jpg 20120407152447 http://cafethumb.naver.net/20101223_84/qkrgns3_129303386816936xUq_jpg/imag0030_qkrgns3.jpg unk 200 OUK52MTLKPEA6STHTFFPFI2JP7G4QBUZ - - 3587 153 bad_mime_type.arc.gz',
         'crlf_at_1k_boundary.warc.gz':    'nz,co,tradeaboat,whitiangamarine)/emailafriend.aspx?item=h4siagw4x00a/wfwao/9gaxg6utmkolwv1zy9nohybsaoj36okttm/cdglv9et4wgw8ywbkoacccfsjvdmf7bge+ke8edgs5h4ib0rue96yj2/r5lixmy1sueue5iihmyms9jl9femizgo6yaew0fx+snckd5d+ow5216i0sj9yb0pzj/i/3z3mannav042wjyfyugogpn6yv2wzgueerk5fqi+msasd88rtsytzkszuc/mtpdowhevxiy3n2+r1n6q9utfvekuy5bonzpqy7blk93yj9dnviit0zjmshgotxc0nuywionfpixfogmm8y6i3rfxxqxd5p95qmiogdi1rvpgkcav+go4nz4r/caicl697pcwfkcqyfw5zts74+snrdessbdz2quceotydcw2gh3hogkrrupiqn9hfdvsb2p3hxp/ygkh9w6+d8jp7tylmalvnjjevst/6wlbqrhwrsnlpxntjxqzrtw7z8e/+o5bfsb6hgwfxzulqz2rnnfvazomgkckthoprtba6cp5ifb8j8sfov7pvwifngclbr28ekmjaebqrznblb4njweisomyenibp/qlvpv4sqarzduhs1qri9toq/toiasrlkpq+sdsbuzqjxij9b/tjgx8biqe129tdob0bdhtexwqq1aoaasxmtqddrykqcrvckjfh1ayszhyl9p6xs6lwmalo2mygxnzegkrvpfr5c/edjp6hr/28egr4fdxyyrwaumhoprqgxyjtq7nqwv7m8jyyvxcfgpx6kz6ftu4nmbahpuhgxd/eddp5y3duicjbcaymmvvmojqxmxb8cpsytv9zcu1rn5ehrp2iypudy+6ihhacaaa= 20110218233256 http://whitiangamarine.tradeaboat.co.nz/emailAFriend.aspx?item=H4sIAGW4X00A%2fwFwAo%2f9gaXg6UTMkoLWV1Zy9nOhybsaOj36okTTM%2fCdGlV9et4wGW8ywbKoacCcFSjvDmf7BgE%2bke8eDGs5H4ib0RuE96Yj2%2fR5LIXmy1SUEue5IiHmYmS9jl9femiZGo6yAeW0fX%2bSnCkd5D%2bOW5216i0SJ9yb0PZJ%2fI%2f3z3manNAv042wJYFyUgOGpN6yV2wZGUEERk5FQI%2bmSASd88RTsytzksZuC%2fmTpDowhevXiY3N2%2br1n6Q9utfvEKuy5bonZPqy7BlK93yJ9DnviiT0ZJMsHGOTXC0NUywIonFpIXfogmm8y6I3RfXxQXD5p95qmiogdI1rvPgKCaV%2bgO4nZ4r%2fCAicl697pcwFKCQyFW5ZTS74%2bSnrdEssBdz2quceotYDcW2GH3hogkrRupiqN9hFdVsb2p3HXP%2fYGkH9W6%2bD8jp7TyLmALvnJJevST%2f6wlbQRhWrsNlPXnTjxQZrTw7z8E%2f%2bo5BFsb6HgWfXzULQZ2RnNFvAZOMgkcKtHopRTbA6cp5ifB8j8sFoV7PVwifNgcLBR28EKMjAeBqRZnBlB4nJwEISomyeNIBP%2fQlvpV4sqArZdUhs1qRi9TOQ%2fToiaSrlKpq%2bSdSbuZqjXIJ9b%2ftjgx8biQe129TDOB0BDHtEXwqq1aoaASxmTqddrYKqCRvcKjfH1aYSZHyL9p6xS6LwMAlO2myGxnZeGkrVpfr5C%2fEDJp6HR%2f28EgR4fdXyyRWauMhoPrQgXYJTq7NQwv7m8JYyvxCfGpX6Kz6ftu4NMBAHPuhGxd%2fEDDP5y3DUIcJBCAyMMvvMOJQXMXb8cpsyTv9ZcU1RN5ehrp2iyPudY%2b6iHHACAAA%3d text/html 200 M4VJCCJQJKPACSSSBHURM572HSDQHO2P - - 2588 0 crlf_at_1k_boundary.warc.gz',
         'crlf_at_1k_boundary_2.warc.gz':  'au,com,grandtourer)/aspx/login.aspx?4=h6vklmshqnbpvsscb7x7iu2/luokwckr5nsukefi3ygag1wtqor9vtiwv+anh9su4shtqmrrjy53dhqpxif+vjqkb+tajvfhn/sn1oqgaxly4i1ciwbi6jbk+i0fqqn44wt18szrgn95ygnruk9baymdquzchh7i/pak180zcfccrud+lqmmukvlvg0qoq6kvbos8dqo3mh5unwoclxiid2+mbma2rfp/015+o5+dnrq/umof3aettvsy7i/bcmgkbn/6wqknr04kfi4ppwjig2vcw4av8hj2fqbo+3jutdryfgyulizuqjebrh0lmah9sgkrpomwa0hgzmvf1ahoyqbvnbwujeekckxrydnd+dtxyozqlpygn/gcedbkoubmmmldsl+stl4qzomxngk3xnxiw+/csq/pwyimcbtdl/fxvnj6j4l3m5v66mjhxmyzk/wfp7spfzeghl+x4ih9dzzl8nqr/+ma7e6jhmyx4/dwkresqh3mzmiqddmdp6cjtnxapulfamv/tdy1vgjdl4pbiasartibf4nnxlglpvcy+cm3j83nybyytxbrx9+x1vcvnvpo8sipspuyp8xi0glnsmaw/u+owll28euzdlvanmz2j0rcdhtqkyejfhn/rm4z1gkhwn2rexkykbgtnuppthr08v6sur9kagw9dzdyut0go9fjshgpbmnm0uaujtzkshhi0uriz2cnn+arsppeayooy3yedrv7vklewh6mj3yjqfzwj4tbq75wecrm9gw4p+7uwal4wc92gjdip7g1p2cm4vbtvahp1ntq+shd4oot5r6hza2igo85st3ftgfvfj7eolin+dixrjdwa== 20120422095915 https://www.grandtourer.com.au/Aspx/Login.aspx?4=H6VKLMsHqnBpvsscB7x7Iu2%2fLUOKwCKr5nsukefI3ygAG1WTqOR9vtiWv%2banh9sU4sHTQmRRJY53DHQpXiF%2bVjqKB%2btaJvfHn%2fSN1OQgaxlY4i1Ciwbi6jbK%2bI0fQqn44Wt18szRgN95ygNRUK9BaYMdqUzChH7I%2fpAk180zCFCCRUD%2bLqMMuKvLVg0qOQ6Kvbos8DqO3MH5UnwOcLxiID2%2bmBMA2Rfp%2f015%2bo5%2bDNRq%2fUMOF3aETtvSY7i%2fbCmGKBn%2f6WqkNr04Kfi4PPWJIg2VCw4AV8hj2FqbO%2b3JUtdRYfGYulizuQJEbrh0LMah9sGKRPomWA0hgZmvf1AHoYqbVNbwUJeEKCKxrYdND%2bDtxyOzQlpygN%2fgCeDbKOuBMMMLdSl%2bsTl4qZoMXnGK3XNxiw%2b%2fcsq%2fPWyIMCBtdl%2ffXvnJ6J4L3M5v66mjhXmyZk%2fwfp7SpfzegHL%2bX4iH9DZzl8nqr%2f%2bmA7E6JHmyX4%2fDWKrEsqH3MZMIqddmDp6cJtnxAPULfAmv%2fTDY1VGJdl4PBIASArTIBF4nnXLglpvcy%2bcm3j83nyByyTxbRX9%2bX1VcVNvPo8SIpSpuYP8xi0GlNsMaW%2fu%2bowll28EUzDLVAnMz2j0rcdhTqKYEJfhN%2frm4Z1gKhwn2REXKykBGTnupPtHR08V6Sur9kAgW9DZdyUt0Go9fJshGPBmNm0uAUjtzkshhI0UrIz2cnn%2bArspPeaYOOY3YEdrV7VKlEWh6Mj3yjQFZwj4TbQ75WECrM9Gw4p%2b7uWaL4wc92gjDiP7G1P2cM4vBTVAHP1nTQ%2bShD4OoT5r6hZA2igo85St3ftgfvfJ7eOLin%2bdixRJdwA%3d%3d text/html 200 5STDGW7HDWZQ4TPS4GPBOL3TEG7NQRHE - - 6934 0 crlf_at_1k_boundary_2.warc.gz', #from NLA-AU-CRAWL-006-20120421051259635-00205-02593-crawling119/NLA-AU-CRAWL-006-20120422094450650-02571-3266~web-crawl001.us.archive.org~8443.warc.gz offset 90441596
         'giant_html.warc.gz':             'com,guide-fleurs)/site/partenaires.htm 20120121173511 http://www.guide-fleurs.com/site/partenaires.htm text/html 200 BGA6K3VEQVACI7KVTAGRNMBAPIYIGELF - - 1882583 0 giant_html.warc.gz',
         'negative_content_length.arc.gz': 'com,lastdaywatchers)/robots.txt 20120420180002 http://www.lastdaywatchers.com/robots.txt text/html 301 3I42H3S6NNFQ2MSVX7XZKYAYSCX5QBYJ http://lastdaywatchers.com/robots.txt/ - 244 155 negative_content_length.arc.gz\ncom,diggheadlines)/robots.txt 20120420180002 http://diggheadlines.com/robots.txt unk 502 3I42H3S6NNFQ2MSVX7XZKYAYSCX5QBYJ - - 103 520 negative_content_length.arc.gz',
         'bad_unicode_host.arc.gz':        'net,82,t%ef%bf%bd%04)/ 20080509130938 http://www.t%EF%BF%BD%04.82.net/ text/html 200 V6CPFAFQFDRK2BWCGRXEZYKAGOUMWYM5 http://nic.82.net - 416 158 bad_unicode_host.arc.gz', #from 1213886081714_1-c/1213886929852_11.arc.gz, contains unicode replacement char
         'non_ascii_url.arc.gz':           'fr,free,arevebebe)/php3/selcateg.php3?selec=%e9cole 20021108114510 http://arevebebe.free.fr/php3/selcateg.php3?selec=école text/html 200 IRZDAFOGADI2OCQFHJGUBL6BELKT37C7 - - 2528 168 non_ascii_url.arc.gz', #from INA-HISTORICAL-2002-GROUP-EVL-20100812000000-00001-c/INA-HISTORICAL-2002-GROUP-FFM-20100812000000-00000.arc.gz. We put a non-ascii char field like the java version, but we utf8-encode the character. Also, the surt seems incorrect. It seems like we should convert the surt to utf-8 before percent encoding..
         '16_digit_date.arc.gz':           'com,afp)/home/img/es.gif 20000823054100 http://www.afp.com:80/home/img/es.gif image/gif 200 FL5ZDSVRACUUD2GUCKOWWY6LPPLR7TSJ - - 936 168 16_digit_date.arc.gz', #from INA-HISTORICAL-1996-GROUP-AAA-20100812000000-00000-c/INA-HISTORICAL-2000-GROUP-ACS-20100812000000-00001.arc.gz
         'alexa_charset_in_header.arc.gz': 'fr,allocine,free)/tv/cineaction.asp 20000824015105 http://free.allocine.fr:80/tv/cineaction.asp text/html 200 YSO3GBFJ7KRO3OPF7J43J4NMM4LVR7ZY - - 3974 168 alexa_charset_in_header.arc.gz', #from INA-HISTORICAL-1996-GROUP-AAA-20100812000000-00000-c/INA-HISTORICAL-2000-GROUP-ACS-20100812000000-00001.arc.gz, fixed in warctools changeset 92:ca95fa09848b
         'chardet_failure_url.arc.gz':     'cn,com,pconline,guide)/gamecomment/post.jsp?column=netgame&topic=%ce%d2%c3%c7%d7%f6%d6%f7%b5%c4%ca%c0%b4%fa%b5%bd%c0%b4%c1%cb%a3%a1%a1%b6%c8%d9%d2%ab%a1%b7%b7%a8%b5%e4%d5q%c9%fa%a3%a1 20040711214255 http://guide.pconline.com.cn:80/gamecomment/post.jsp?column=netgame&topic=\xe6\x88\x91\xe4\xbb\xac\xe5\x81\x9a\xe4\xb8\xbb\xe7\x9a\x84\xe4\xb8\x96\xe4\xbb\xa3\xe5\x88\xb0\xe6\x9d\xa5\xe4\xba\x86\xef\xbc\x81\xe3\x80\x8a\xe8\x8d\xa3\xe8\x80\x80\xe3\x80\x8b\xe6\xb3\x95\xe5\x85\xb8\xef\xbf\xbd\xe7\x94\x9f\xef\xbc\x81 text/html 400 YVY3QUSAB6EOL5HYRV3CNKRMZZ6U6K2E - - 485 153 chardet_failure_url.arc.gz', #from DX_crawl29.20040711143227-c/DX_crawl29.20040711214146.arc.gz
         'formfeed_in_url.arc.gz':         'com,megaclick)/notf!%ca%9d%f5%99s%19%f1d%ef%96%03x%92%8d%a7%1d%99%f9!%d7%97/%8c%1c52%fa%f9%f2b%e2%89u%dc%ad2 20070519230830 http://www.megaclick.com:80/notf!\xce\x9a\xc2\x9d\xcf\x85\xc2\x99s\x19\xcf\x81d\xce\xbf\xc2\x96\x03X\xc2\x92\xc2\x8d\xc2\xa7\x1d\xc2\x99\xcf\x89!\xce\xa7\xc2\x97/\xc2\x8c\x1c52\xcf\x8a\xcf\x89\xcf\x82b\xce\xb2\xc2\x89u\xce\xac\xc2\xad2#l\xc2\x8a\xef\xbf\xbd\xce\xa9\xce\xaf\xc2\xbd\x05;2z\xc2\x91\x10r\x0c\xce\x9f9\xce\x8e text/html 404 QTPHGEGAVG7NTUMH3UQF2YGQHZ27VGML - - 445 159 formfeed_in_url.arc.gz', #from 42_0_20070519125725_crawl29-c/42_0_20070519230217_crawl31.arc.gz
        }

for file, cdx in warcs.iteritems():

    warc_file = quote(file)
    assert os.path.exists(warc_file)

    print "processing", warc_file

    cmd = '../cdx_writer.py %s' % warc_file
    print "  running", cmd
    status, output = commands.getstatusoutput(cmd)
    assert 0 == status


    assert output.endswith(cdx)

print "exiting without errors!"
