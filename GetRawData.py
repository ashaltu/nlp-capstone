from opustools_pkg import OpusGet, OpusRead
import os

def add_to_root_dir(corpus=None, source=None, target=None,
        version='latest', preprocess=None, root_dir=None):

    OpusGet(directory=corpus, source=source, target=target, release=version,
        preprocess=preprocess, download_dir=root_dir, suppress_prompts=True,
        ).get_files()

    print(root_dir, corpus, version, preprocess, target+'.zip')
    source_zip = '{corpus}_{version}_{preprocess}_{source}.zip'.format(
        corpus=corpus, version=version, preprocess=preprocess, source=source)
    os.rename(os.path.join(root_dir, source_zip),
        os.path.join(root_dir, corpus, version, preprocess, source+'.zip'))

    target_zip = '{corpus}_{version}_{preprocess}_{target}.zip'.format(
        corpus=corpus, version=version, preprocess=preprocess, target=target)
    os.rename(os.path.join(root_dir,target_zip),
        os.path.join(root_dir, corpus, version, preprocess, target+'.zip'))

    alignment_xml = ('{corpus}_{version}_{preprocess}_{source}-'
        '{target}.xml.gz').format(corpus=corpus, version=version,
            preprocess='xml', source=source, target=target)
    os.rename(os.path.join(root_dir, alignment_xml),
        os.path.join(root_dir, corpus, version, 'xml',
            source+'-'+target+'.xml.gz'))
    
add_to_root_dir(corpus='WikiMatrix', source='ca', target='it',
                preprocess='xml', root_dir='/mnt/c/Work/CSE481N/data/')

OpusRead(directory='WikiMatrix', source='ca', target='it',
            write=[os.path.join('/mnt/c/Work/CSE481N/data/', 'test_files', 'ca-it.ca'),
                    os.path.join('/mnt/c/Work/CSE481N/data/', 'test_files', 'ca-it.it')],
            write_mode='moses' ,root_directory='/mnt/c/Work/CSE481N/data/').printPairs()

add_to_root_dir(corpus='ParaCrawl', source='ca', target='es',
                preprocess='xml', root_dir='/mnt/c/Work/CSE481N/data/')

OpusRead(directory='ParaCrawl', source='ca', target='es',
            write=[os.path.join('/mnt/c/Work/CSE481N/data/', 'test_files', 'ca-es.ca'),
                    os.path.join('/mnt/c/Work/CSE481N/data/', 'test_files', 'ca-es.es')],
            write_mode='moses' ,root_directory='/mnt/c/Work/CSE481N/data/').printPairs()

add_to_root_dir(corpus='MultiCCAligned', source='es', target='it',
                preprocess='xml', root_dir='/mnt/c/Work/CSE481N/data/')

OpusRead(directory='MultiCCAligned', source='es', target='it',
            write=[os.path.join('/mnt/c/Work/CSE481N/data/', 'test_files', 'es-it.es'),
                    os.path.join('/mnt/c/Work/CSE481N/data/', 'test_files', 'es-it.it')],
            write_mode='moses' ,root_directory='/mnt/c/Work/CSE481N/data/').printPairs()
