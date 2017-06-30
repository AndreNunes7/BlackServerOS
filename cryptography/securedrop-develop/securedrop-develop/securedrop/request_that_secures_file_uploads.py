from io import BytesIO

from flask import wrappers

from secure_tempfile import SecureTemporaryFile


class RequestThatSecuresFileUploads(wrappers.Request):

    def _secure_file_stream(self, total_content_length, content_type,
                            filename=None, content_length=None):
        """Storage class for data streamed in from requests.

        If the data is relatively small (512KB), just store it in
        memory. Otherwise, use the SecureTemporaryFile class to buffer
        it on disk, encrypted with an ephemeral key to mitigate
        forensic recovery of the plaintext.

        """
        if total_content_length > 1024 * 512:
            # We don't use `config.TEMP_DIR` here because that
            # directory is exposed via X-Send-File and there is no
            # reason for these files to be publicly accessible. See
            # note in `config.py` for more info. Instead, we just use
            # `/tmp`, which has the additional benefit of being
            # automatically cleared on reboot.
            return SecureTemporaryFile('/tmp')
        return BytesIO()

    def make_form_data_parser(self):
        return self.form_data_parser_class(self._secure_file_stream,
                                           self.charset,
                                           self.encoding_errors,
                                           self.max_form_memory_size,
                                           self.max_content_length,
                                           self.parameter_storage_class)
