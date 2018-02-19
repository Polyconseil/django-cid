Settings
========

.. glossary::
    :sorted:

    ``CID_HEADER``
        The HTTP header to extract the correlation id from. Default value:
        ``X_CORRELATION_ID``

    ``CID_RESPONSE_HEADER``
        The HTTP *response* header where the correlation id will be set.
        Default value: same name as ``CID_HEADER``. Set to ``None`` if
        you do not want the response to include the header.

    ``CID_GENERATE``
        Tell the cid middleware to generate a correlation id if it doesn't
        already exist. Default value: ``False``.

    ``CID_SQL_COMMENT_FORMATTER``
        Function taking a cid as argument and returning the str that will be
        added as a SQL comment. Default returned value: ``cid: MY_CID``.
