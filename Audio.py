#! /usr/bin/env python
# -*- coding: utf-8 -*-

from wave import open as waveOpen
from ossaudiodev import open as ossOpen

#klasa Audio obsługuje pliki wav i odtwarza je
class Audio(object):
	def play(self, wav_file):
		try:
			stream = waveOpen(wav_file,'rb')
			(nc,sw,fr,nf,comptype, compname) = stream.getparams()
			dsp_device = ossOpen('/dev/dsp','w')
			try:
				from ossaudiodev import AFMT_S16_NE
			except ImportError:
				if byteorder == "little":
					AFMT_S16_NE = ossaudiodev.AFMT_S16_LE
				else:
					AFMT_S16_NE = ossaudiodev.AFMT_S16_BE
			dsp_device.setparameters(AFMT_S16_NE, nc, fr)
			data = stream.readframes(nf)
			stream.close()
			dsp_device.write(data)
			dsp_device.close()
		except:
			print "Błąd: Wystąpił problem podczas odtwarzania pliku audio !!!"


#testowanie
if __name__ == "__main__":
	pass

