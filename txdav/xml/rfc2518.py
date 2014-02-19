##
# Copyright (c) 2005-2014 Apple Inc. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
##

# FIXME: RFC 2518 is obsoleted by RFC 5689.  Check for changes.

"""
RFC 2518 (WebDAV) XML Elements

This module provides XML element definitions for use with WebDAV.

See RFC 2518: http://www.ietf.org/rfc/rfc2518.txt
"""

__all__ = []


from txweb2 import responsecode
from txweb2.http_headers import MimeType

from txdav.xml.base import WebDAVElement, WebDAVTextElement, PCDATAElement
from txdav.xml.base import WebDAVEmptyElement, WebDAVOneShotElement
from txdav.xml.base import WebDAVDateTimeElement, DateTimeHeaderElement
from txdav.xml.element import dav_namespace, registerElement, registerElementClass


##
# Section 12
##

@registerElement
@registerElementClass
class ActiveLock (WebDAVElement):
    """
    Describes a lock on a resource. (RFC 2518, section 12.1)
    """
    name = "activelock"

    allowed_children = {
        (dav_namespace, "lockscope"): (1, 1),
        (dav_namespace, "locktype"): (1, 1),
        (dav_namespace, "depth"): (1, 1),
        (dav_namespace, "owner"): (0, 1),
        (dav_namespace, "timeout"): (0, 1),
        (dav_namespace, "locktoken"): (0, 1),
    }



@registerElement
@registerElementClass
class Depth (WebDAVTextElement):
    """
    The value of the depth header. (RFC 2518, section 12.1.1)
    """
    name = "depth"

    def validate(self):
        super(Depth, self).validate()

        depth = str(self)
        if depth not in ("0", "1", "infinity"):
            raise ValueError("Invalid depth: %s" % (depth,))



@registerElement
@registerElementClass
class LockToken (WebDAVElement):
    """
    The lock token associated with a lock. (RFC 2518, section 12.1.2)
    """
    name = "locktoken"

    allowed_children = {(dav_namespace, "href"): (1, None)}



@registerElement
@registerElementClass
class Timeout (WebDAVTextElement):
    """
    The timeout associated with a lock. (RFC 2518, section 12.1.3)
    """
    name = "timeout"



@registerElement
@registerElementClass
class Collection (WebDAVEmptyElement):
    """
    Identifies the associated resource as a collection. (RFC 2518, section 12.2)
    """
    name = "collection"



@registerElement
@registerElementClass
class HRef (WebDAVTextElement):
    """
    Identifies the content of the element as a URI. (RFC 2518, section 12.3)
    """
    name = "href"



@registerElement
@registerElementClass
class Link (WebDAVElement):
    """
    Identifies the property as a link and contains the source and
    destination of that link. (RFC 2518, section 12.4)
    """
    name = "link"

    allowed_children = {
        (dav_namespace, "src"): (1, None),
        (dav_namespace, "dst"): (1, None),
    }



@registerElement
@registerElementClass
class LinkDestination (WebDAVTextElement):
    """
    Indicates the destination of a link. (RFC 2518, section 12.4.1)
    """
    name = "dst"



@registerElement
@registerElementClass
class LinkSource (WebDAVTextElement):
    """
    Indicates the source of a link. (RFC 2518, section 12.4.2)
    """
    name = "src"



@registerElement
@registerElementClass
class LockEntry (WebDAVElement):
    """
    Defines the types of lock that can be used with the
    resource. (RFC 2518, section 12.5)
    """
    name = "lockentry"

    allowed_children = {
        (dav_namespace, "lockscope"): (1, 1),
        (dav_namespace, "locktype"): (1, 1),
    }



@registerElement
@registerElementClass
class LockInfo (WebDAVElement):
    """
    Used with a LOCK method to specify the type of lock that the
    client wishes to have created. (RFC 2518, section 12.6)
    """
    name = "lockinfo"

    allowed_children = {
        (dav_namespace, "lockscope"): (1, 1),
        (dav_namespace, "locktype"): (1, 1),
        (dav_namespace, "owner"): (0, 1),
    }



@registerElement
@registerElementClass
class LockScope (WebDAVOneShotElement):
    """
    Specifies whether a lock is an exclusive lock or a shared
    lock. (RFC 2518, section 12.7)
    """
    name = "lockscope"

    allowed_children = {
        (dav_namespace, "exclusive"): (0, 1),
        (dav_namespace, "shared"): (0, 1),
    }



@registerElement
@registerElementClass
class Exclusive (WebDAVEmptyElement):
    """
    Indicates an exclusive lock. (RFC 2518, section 12.7.1)
    """
    name = "exclusive"

LockScope.exclusive = LockScope(Exclusive())


@registerElement
@registerElementClass
class Shared (WebDAVEmptyElement):
    """
    Indicates a shared lock. (RFC 2518, section 12.7.2)
    """
    name = "shared"

LockScope.shared = LockScope(Shared())


@registerElement
@registerElementClass
class LockType (WebDAVOneShotElement):
    """
    Specifies the access type of a lock. (RFC 2518, section 12.8)
    """
    name = "locktype"

    allowed_children = {(dav_namespace, "write"): (0, 1)}



@registerElement
@registerElementClass
class Write (WebDAVEmptyElement):
    """
    Indicates a write lock. (RFC 2518, section 12.8.1)
    Controls methods that lock a resource or modify the content, dead
    properties, or (in the case of a collection) membership of a resource.
    (RFC 3744, section 3.2)
    """
    name = "write"

LockType.write = LockType(Write())



@registerElement
@registerElementClass
class MultiStatus (WebDAVElement):
    """
    Contains multiple Responses. (RFC 2518, section 12.9)
    """
    name = "multistatus"

    allowed_children = {
        (dav_namespace, "response"): (0, None),
        (dav_namespace, "responsedescription"): (0, 1),
    }



@registerElement
@registerElementClass
class Response (WebDAVElement):
    """
    Holds a single response describing the effect of a method on a
    resource and/or its properties. (RFC 2518, section 12.9.1)
    """
    name = "response"

    allowed_children = {
        (dav_namespace, "href"): (1, None),
        (dav_namespace, "status"): (1, 1),
        (dav_namespace, "propstat"): (1, None),
        (dav_namespace, "error"): (0, 1),        # 2518bis
        (dav_namespace, "responsedescription"): (0, 1),
    }

    def __new__(cls, *children):
        if cls is not Response:
            return WebDAVElement.__new__(cls)

        resource_count = 0
        status_count = 0
        propstat_count = 0

        for child in children:
            if   isinstance(child, HRef):
                resource_count += 1
            elif isinstance(child, Status):
                status_count += 1
            elif isinstance(child, PropertyStatus):
                propstat_count += 1

        if resource_count < 1:
            raise ValueError("%s element must have at least one %s."
                             % (cls.sname(), HRef.sname()))

        if status_count is 0:
            if propstat_count is 0:
                raise ValueError("%s element must have one of %s or %s"
                                 % (cls.sname(), Status.sname(), PropertyStatus.sname()))

            if resource_count > 1:
                raise ValueError("%s element with %s may only have one %s"
                                 % (cls.sname(), PropertyStatus.sname(), HRef.sname()))

            return PropertyStatusResponse.__new__(PropertyStatusResponse, *children)

        if status_count > 1:
            raise ValueError("%s element may only have one %s" % (cls.sname(), Status.sname()))

        return StatusResponse.__new__(StatusResponse, *children)



@registerElementClass
class StatusResponse (Response):
    """
    Specialized derivative of Response for resource status.
    """
    unregistered = True

    allowed_children = {
        (dav_namespace, "href"): (1, None),
        (dav_namespace, "status"): (1, 1),
        (dav_namespace, "error"): (0, 1),        # 2518bis
        (dav_namespace, "responsedescription"): (0, 1),
    }



@registerElementClass
class PropertyStatusResponse (Response):
    """
    Specialized derivative of Response for property status.
    """
    unregistered = True

    allowed_children = {
        (dav_namespace, "href"): (1, 1),
        (dav_namespace, "propstat"): (1, None),
        (dav_namespace, "error"): (0, 1),        # 2518bis
        (dav_namespace, "responsedescription"): (0, 1),
    }



@registerElement
@registerElementClass
class PropertyStatus (WebDAVElement):
    """
    Groups together a Property and Status element that is associated
    with a particular DAV:href element. (RFC 2518, section 12.9.1.1)
    """
    name = "propstat"

    allowed_children = {
        (dav_namespace, "prop"): (1, 1),
        (dav_namespace, "status"): (1, 1),
        (dav_namespace, "error"): (0, 1),        # 2518bis
        (dav_namespace, "responsedescription"): (0, 1),
    }



@registerElement
@registerElementClass
class Status (WebDAVTextElement):
    """
    Holds a single HTTP status line. (RFC 2518, section 12.9.1.2)
    """
    name = "status"

    @classmethod
    def fromResponseCode(cls, code):
        """
        code must be an integer response code in
        txweb2.responsecode.RESPONSES.keys()
        """
        if code not in responsecode.RESPONSES:
            raise ValueError("Invalid response code: %r" % (code,))

        return cls(PCDATAElement("HTTP/1.1 %d %s" % (code, responsecode.RESPONSES[code])))


    def __init__(self, *children, **attributes):
        super(Status, self).__init__(*children, **attributes)

        status = str(self)
        if not status.startswith("HTTP/1.1 "):
            raise ValueError("Invalid WebDAV status: %s" % (status,))

        code = int(status[9:12])
        if code not in responsecode.RESPONSES:
            raise ValueError("Invalid status code: %s" % (code,))

        self.code = code



@registerElement
@registerElementClass
class ResponseDescription (WebDAVTextElement):
    """
    Contains a message that can be displayed to the user explaining the nature
    of the response. (RFC 2518, section 12.9.2)
    """
    name = "responsedescription"



@registerElement
@registerElementClass
class Owner (WebDAVElement):
    """
    Property which provides information about the principal taking out a lock.
    (RFC 2518, section 12.10)
    Property which identifies a principal as being the owner principal of a
    resource. (RFC 3744, section 5.1)
    Note that RFC 2518 allows any content, while RFC 3744 expect zero or one
    DAV:href element.
    """
    name = "owner"
    hidden = True
    protected = True # may be protected, per RFC 3744, section 5.1

    allowed_children = {WebDAVElement: (0, None)}



@registerElement
@registerElementClass
class PropertyContainer (WebDAVElement):
    """
    Contains properties related to a resource. (RFC 2518, section 12.11)
    """
    name = "prop"

    allowed_children = {WebDAVElement: (0, None)}



@registerElement
@registerElementClass
class PropertyBehavior (WebDAVElement):
    """
    Specifies how properties are handled during a COPY or MOVE. (RFC 2518,
    section 12.12)
    """
    name = "propertybehavior"

    allowed_children = {
        (dav_namespace, "omit"): (0, 1),
        (dav_namespace, "keepalive"): (0, 1),
    }


    def __init__(self, *children, **attributes):
        super(PropertyBehavior, self).__init__(*children, **attributes)

        if len(self.children) != 1:
            raise ValueError(
                "Exactly one of DAV:omit, DAV:keepalive required for %s, got: %s"
                % (self.sname(), self.children)
            )

        self.behavior = children[0]



@registerElement
@registerElementClass
class KeepAlive (WebDAVElement):
    """
    Specifies requirements for the copying/moving or live properties. (RFC 2518,
    section 12.12.1)
    """
    name = "keepalive"

    allowed_children = {
        (dav_namespace, "href"): (0, None),
        PCDATAElement: (0, 1),
    }


    def validate(self):
        super(KeepAlive, self).validate()

        type = None

        for child in self.children:
            if type is None:
                type = child.qname()
            elif child.qname() != type:
                raise ValueError(
                    "Only one of DAV:href or PCDATA allowed for %s, got: %s"
                    % (self.sname(), self.children)
                )

        if type == "#PCDATA":
            if str(self) != "*":
                raise ValueError("Invalid keepalive value: %r", (str(self),))



@registerElement
@registerElementClass
class Omit (WebDAVEmptyElement):
    """
    Instructs the server that it should use best effort to copy properties. (RFC
    2518, section 12.12.2)
    """
    name = "omit"



@registerElement
@registerElementClass
class PropertyUpdate (WebDAVElement):
    """
    Contains a request to alter the properties on a resource. (RFC 2518, section
    12.13)
    """
    name = "propertyupdate"

    allowed_children = {
        (dav_namespace, "remove"): (0, None),
        (dav_namespace, "set"): (0, None),
    }



@registerElement
@registerElementClass
class Remove (WebDAVElement):
    """
    Lists the DAV properties to be removed from a resource. (RFC 2518, section
    12.13.1)
    """
    name = "remove"

    allowed_children = {(dav_namespace, "prop"): (1, 1)}



@registerElement
@registerElementClass
class Set (WebDAVElement):
    """
    Lists the DAV properties to be set for a resource. (RFC 2518, section
    12.13.2)
    """
    name = "set"

    allowed_children = {(dav_namespace, "prop"): (1, 1)}



@registerElement
@registerElementClass
class PropertyFind (WebDAVElement):
    """
    Specifies the properties to be returned from a PROPFIND
    method. (RFC 2518, section 12.14)
    """
    name = "propfind"

    allowed_children = {
        (dav_namespace, "allprop"): (0, 1),
        (dav_namespace, "propname"): (0, 1),
        (dav_namespace, "prop"): (0, 1),
    }


    def validate(self):
        super(PropertyFind, self).validate()

        if len(self.children) != 1:
            raise ValueError(
                "Exactly one of DAV:allprop, DAV:propname or DAV:prop is required for %s, got: %r"
                % (self.sname(), self.children)
            )



@registerElement
@registerElementClass
class AllProperties (WebDAVEmptyElement):
    """
    Specifies that all property names and values on the resource are
    to be returned. (RFC 2518, section 12.14.1)
    """
    name = "allprop"



@registerElement
@registerElementClass
class PropertyName (WebDAVEmptyElement):
    """
    Specifies that only a list of property names on the resource are
    to be returned. (RFC 2518, section 12.14.2)
    """
    name = "propname"



##
# Section 13
##

@registerElement
@registerElementClass
class CreationDate (WebDAVDateTimeElement):
    """
    Records the time and date that the resource was created. (RFC 2518, section
    13.1)
    """
    name = "creationdate"
    # MAY be protected as per RFC2518bis.  We may make this more flexible later.
    protected = True



@registerElement
@registerElementClass
class DisplayName (WebDAVTextElement):
    """
    Provides a name for the resource that is suitable for presentation
    to a user. (RFC 2518, section 13.2)
    """
    name = "displayname"



@registerElement
@registerElementClass
class GETContentLanguage (WebDAVTextElement):
    """
    Contains the Content-Language header returned by a GET without
    accept headers. (RFC 2518, section 13.3)
    """
    name = "getcontentlanguage"



@registerElement
@registerElementClass
class GETContentLength (WebDAVTextElement):
    """
    Contains the Content-Length header returned by a GET without
    accept headers. (RFC 2518, section 13.4)
    """
    name = "getcontentlength"
    protected = True



@registerElement
@registerElementClass
class GETContentType (WebDAVTextElement):
    """
    Contains the Content-Type header returned by a GET without
    accept headers. (RFC 2518, section 13.5)
    """
    name = "getcontenttype"

    def mimeType(self):
        return MimeType.fromString(str(self))



@registerElement
@registerElementClass
class GETETag (WebDAVTextElement):
    """
    Contains the ETag header returned by a GET without
    accept headers. (RFC 2518, section 13.6)
    """
    name = "getetag"
    protected = True



@registerElement
@registerElementClass
class GETLastModified (DateTimeHeaderElement):
    """
    Contains the Last-Modified header returned by a GET without accept
    headers. (RFC 2518, section 13.7)
    """
    name = "getlastmodified"
    protected = True



@registerElement
@registerElementClass
class LockDiscovery (WebDAVElement):
    """
    Describes the active locks on a resource. (RFC 2518, section 13.8)
    """
    name = "lockdiscovery"
    protected = True

    allowed_children = {(dav_namespace, "activelock"): (0, None)}



@registerElement
@registerElementClass
class ResourceType (WebDAVElement):
    """
    Specifies the nature of the resource. (RFC 2518, section 13.9)
    """
    name = "resourcetype"
    protected = True

    allowed_children = {WebDAVElement: (0, None)}

ResourceType.collection = ResourceType(Collection())
ResourceType.empty = ResourceType()


@registerElement
@registerElementClass
class Source (WebDAVElement):
    """
    The destination of the source link identifies the resource that
    contains the unprocessed source of the link's source. (RFC 2518, section
    13.10)
    """
    name = "source"

    allowed_children = {(dav_namespace, "link"): (0, None)}



@registerElement
@registerElementClass
class SupportedLock (WebDAVElement):
    """
    Provides a listing of the lock capabilities supported by the
    resource. (RFC 2518, section 13.11)
    """
    name = "supportedlock"
    protected = True

    allowed_children = {(dav_namespace, "lockentry"): (0, None)}



# FIXME: Add preconditions codes defined in RFC4918

@registerElement
@registerElementClass
class PropfindFiniteDepth (WebDAVEmptyElement):
    """
    Error which indicates Depth:infinity PROPFIND not allowed
    """
    name = "propfind-finite-depth"
