import os
import tarfile
import zipfile

from pkginfo.distribution import Distribution

class SDist(Distribution):

    def __init__(self, filename, metadata_version=None):
        self.filename = filename
        self.metadata_version = metadata_version
        self.extractMetadata()

    def read(self):
        fqn = os.path.abspath(
                os.path.normpath(self.filename))
        if not os.path.exists(fqn):
            raise ValueError('No such file: %s' % fqn)

        if fqn.endswith('.zip'):
            archive = zipfile.ZipFile(fqn)
            names = archive.namelist()
            def read_file(name):
                return archive.read(name)
        elif fqn.endswith('gz') or fqn.endswith('bz2'):
            archive = tarfile.TarFile.open(fqn)
            names = archive.getnames()
            def read_file(name):
                return archive.extractfile(name).read()
        else:
            raise ValueError('Not a known archive format: %s' % fqn)

        tuples = [x.split('/') for x in names if 'PKG-INFO' in x]
        schwarz = sorted([(len(x), x) for x in tuples])
        for path in [x[1] for x in schwarz]:
            candidate = '/'.join(path)
            data = read_file(candidate)
            if 'Metadata-Version' in data:
                return data

        raise ValueError('No PKG-INFO in archive: %s' % fqn)
