from setuptools import setup

setup(
    name='lektor-hidden-attachments',
    version='0.1',
    author=u'Nathan Yergler',
    author_email='nathan@yergler.net',
    url='https://github.com/nyergler/lektor-hidden-attachments',
    license='MIT',
    py_modules=['lektor_hidden_attachments'],
    entry_points={
        'lektor.plugins': [
            'hidden-attachments = lektor_hidden_attachments:HiddenAttachmentsPlugin',
        ]
    }
)
