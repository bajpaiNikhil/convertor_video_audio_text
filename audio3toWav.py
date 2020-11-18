# import textwrap
# #
# # from pydub import AudioSegment
# #
# # src='audio.mp3'
# # dst="okaudio.wav"
# # sound=AudioSegment.from_mp3(src)
# #
# # sound.export(dst,format="wav")
# d={'a':[{'b':"cbd"}],'f':True}
#
# print(d['a'][0]['b'])
#
# s=d['a'][0]['b']
# print("\n".join(textwrap.wrap(s,1)))

#
# import pyspeedtest
# st = pyspeedtest.SpeedTest()
#
# st.ping()


import speedtest


def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

def main():
    # write to csv
    with open('file.csv', 'w') as f:
        f.write('download,upload,ping\n')
        for i in range(3):
            print('Making test #{}'.format(i+1))
            d, u, p = test()
            f.write('{},{},{}\n'.format(d, u, p))
    # pretty write to txt file
    with open('file.txt', 'w') as f:
        for i in range(3):
            print('Making test #{}'.format(i+1))
            d, u, p = test()
            f.write('Test #{}\n'.format(i+1))
            f.write('Download: {:.2f} Kb/s\n'.format(d / 1024))
            f.write('Upload: {:.2f} Kb/s\n'.format(u / 1024))
            f.write('Ping: {}\n'.format(p))
    # simply print in needed format if you want to use pipe-style: python script.py > file
    for i in range(3):
        d, u, p = test()
        print('Test #{}\n'.format(i+1))
        print('Download: {:.2f} Kb/s\n'.format(d / 1024))
        print('Upload: {:.2f} Kb/s\n'.format(u / 1024))
        print('Ping: {}\n'.format(p))


if __name__ == '__main__':
    main()