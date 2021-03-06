
/*
 * pkey.h
 *
 * Copyright (C) AB Strakt 2001, All rights reserved
 *
 * Export pkey functions and data structure.
 * See the file RATIONALE for a short explanation of why this module was written.
 *
 * @(#) $Id: pkey.h,v 1.3 2008/07/08 10:54:54 acasajus Exp $
 */
#ifndef PyGSI_crypto_PKEY_H_
#define PyGSI_crypto_PKEY_H_

extern int init_crypto_pkey( PyObject * );

extern PyTypeObject crypto_PKey_Type;

#define crypto_PKey_Check(v) ((v)->ob_type == &crypto_PKey_Type)

typedef struct
{
    PyObject_HEAD EVP_PKEY *pkey;
    int dealloc;
} crypto_PKeyObj;

#define crypto_TYPE_RSA           EVP_PKEY_RSA
#define crypto_TYPE_DSA           EVP_PKEY_DSA

#endif
