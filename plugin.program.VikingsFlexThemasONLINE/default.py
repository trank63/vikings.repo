# -*- coding: utf-8 -*-
import base64, codecs
magic = '\x53\x4a\x6c\x57\x53\x67\x6f\x51\x44\x70\x41\x79\x4a\x6e\x41\x43\x4c\x67\x63\x69\x63\x63\x64\x43\x49\x6f\x41\x53\x5a\x6a\x46\x47\x62\x77\x56\x6d\x63\x67\x34\x43\x49\x70\x41\x79\x4a\x6e\x41\x43\x4c\x67\x63\x69\x62\x63\x64\x43\x49\x6f\x41\x53\x5a\x6a\x46\x47\x62\x77\x56\x6d\x63\x67\x34\x43\x49\x70\x41\x69\x49\x30\x68\x48\x64\x75\x45\x57\x62\x6c\x52\x33\x4c\x70\x52\x32\x62\x72\x39\x69\x63\x68\x78\x57\x64\x74\x56\x32\x4c\x74\x39\x32\x59\x75\x4d\x58\x59\x6a\x46\x6d\x63\x6e\x39\x57\x61\x6e\x4a\x58\x5a\x7a\x39\x79\x4c\x36\x41\x48\x64\x30\x68\x6d\x49\x67\x67\x43\x49\x4d\x4a\x56\x56\x66\x35\x55\x52\x51\x39\x45\x49\x75\x41\x69\x62\x76\x31\x57\x62\x76\x4e\x47\x49\x39\x41\x53\x53\x70\x46\x54\x4d\x78\x6b\x55\x53\x4a\x6c\x57\x61\x4a\x42\x69\x43\x4e\x6f\x44\x49\x70\x41\x43\x4b\x67\x6b\x55\x4d\x70\x6c\x45\x49\x6d\x56\x47\x5a\x4b\x30\x51\x61\x78\x45\x54\x61\x4a\x6c\x57\x61\x70\x6c\x47\x49\x72\x41\x79\x62\x50\x39\x30\x54\x77\x38\x32\x62\x77\x38\x30\x62\x50\x39\x47\x49\x75\x41\x79\x62\x77\x41\x7a\x62\x50\x39\x47\x4d\x77\x38\x32\x62\x50\x42\x69\x4b\x67\x38\x32\x62\x50\x42\x7a\x54\x77\x38\x32\x54\x76\x42\x53\x4a\x67\x38\x32\x54\x76\x42\x44\x4d\x50\x39\x30\x62\x76\x42\x53\x4c\x67\x41\x7a\x54\x67\x6f\x54\x4f\x7a\x41\x53\x4c\x67\x6b\x7a\x4d\x67\x59\x57\x61\x4b\x30\x51\x4b\x67\x67\x43\x49\x6e\x39\x47\x62\x68\x6c\x47\x52\x67\x34\x43\x49\x70\x56\x33\x5a\x6a\x31\x6d\x59\x34\x42\x53\x50\x67\x6b\x57\x53\x78\x6b\x55\x61\x70\x6c\x57\x53\x78\x6b\x57\x53\x4a\x70\x51\x44\x70\x41\x53\x58\x67\x51\x44\x49\x36\x41\x79\x57\x67\x6b\x43\x49\x69\x34\x32\x62\x70\x4e\x6e\x63\x6c\x5a\x46\x5a\x73\x6c\x57\x64\x43\x35\x53\x62\x6c\x52\x33\x63\x35\x4e\x6c\x49\x67\x67\x43\x49\x73\x56\x6d\x59\x68\x78\x30\x62\x6d\x35\x57\x53\x30\x56\x32\x5a\x67\x34\x43\x49\x6a\x31\x6d\x59\x34\x42\x43\x4b\x67\x51\x58\x59\x76\x78\x6d\x5a\x67\x30\x44\x49\x4a\x6c\x57\x61\x4a\x46\x54\x53\x4b\x30\x51\x4b\x67\x63\x53\x5a\x74\x46\x6d\x62\x6e\x41\x43\x4b\x67\x38\x6d\x5a\x75\x6c\x6b\x62\x76\x52\x47\x5a\x42\x52\x58\x5a\x6e\x42\x69\x4c\x67\x6b\x43\x49\x6f\x41\x69\x62\x76\x52\x47\x5a\x42\x42\x69\x4c\x67\x34\x32\x62\x6b\x52\x57\x59\x6a\x31\x6d\x59\x34\x42\x53\x50\x67\x41\x44\x4d\x76\x39\x32\x62\x76\x39\x47\x4d\x77\x38\x6b\x43\x4e\x6b\x43\x49\x6e\x34\x32\x62\x70\x4e\x6e\x63\x6c\x5a\x33\x4a\x67\x67\x43\x49\x76\x5a\x6d\x62\x4a\x35\x32\x62\x6b\x52\x57\x51\x30\x56\x32\x5a\x67\x34\x43\x49\x70\x41\x43\x4b\x67\x34\x32\x62\x6b\x52\x57\x51\x67\x34\x43\x49\x75\x39\x47\x5a\x6b\x46\x32\x59\x74\x4a\x47\x65\x67\x30\x44\x49\x78\x6b\x55\x53\x4b\x30\x51\x4b\x67\x63\x79\x4c\x6c\x31\x32\x62\x6f\x39\x79\x4c\x36\x77\x57\x59\x70\x4e\x57\x5a\x77\x4e\x33\x4a\x67\x67\x43\x49\x6f\x52\x58\x59\x51\x56\x47\x64\x68\x78\x32\x63\x75\x46\x6d\x63\x30\x42\x69\x4c\x67\x4d\x57\x62\x69\x68\x48\x49\x39\x41\x79\x54\x50\x42\x7a\x62\x76\x39\x6d\x43\x4e\x6b\x43\x49\x70\x41\x79\x62\x77\x38\x30\x54\x67\x73\x43\x49\x6e\x38\x79\x63\x75\x39\x47\x5a\x6b\x46\x32\x4c\x6c\x31\x32\x62\x6f\x39\x79\x4c\x36\x77\x57\x59\x70\x4e\x57\x5a\x77\x4e\x33\x4a\x67\x67\x43\x49\x75\x6c\x32\x62\x71\x42\x69\x4c\x67\x67\x47\x64\x68\x42\x48\x49\x75\x41\x79\x63\x76\x42\x43\x4b\x67\x67\x47\x64\x68\x42\x56\x5a\x30\x46\x47\x62\x7a\x35\x57\x59\x79\x52\x48\x49\x75\x41\x79\x59\x74\x4a\x47\x65\x67\x30\x44\x49\x70\x6c\x57\x61\x70\x6c\x6d\x43\x4e\x6b\x43\x49\x6e\x55\x57\x62\x68\x35\x32\x4a\x67\x67\x43\x49\x76\x5a\x6d\x62\x4a\x35\x32\x62\x6b\x52\x57\x51\x30\x56\x32\x5a\x67\x34\x43\x49\x76\x39\x32\x54\x77\x38\x32\x54\x67\x30\x44\x49\x77\x38\x45\x4d\x50\x42\x7a\x54\x50\x42\x7a\x54\x77\x38\x6b\x43\x4e\x6b\x43\x49\x76\x42\x7a\x54\x50\x42\x53\x50\x67\x51\x57\x61\x67\x67\x43\x49\x75\x39\x47\x5a\x6b\x46\x45\x49\x75\x41\x69\x62\x76\x52\x47\x5a\x68\x4e\x57\x62\x69\x68\x48\x49\x39\x41\x79\x62\x76\x39\x45\x4d\x76\x39\x6b\x43\x4e\x6b\x43\x49\x6e\x51\x57\x61\x6e\x41\x43\x4b\x67\x38\x6d\x5a\x75\x6c\x6b\x62\x76\x52\x47\x5a\x42\x52\x58\x5a\x6e\x42\x69\x4c\x67\x6b\x43\x49\x6f\x41\x69\x62\x76\x52\x47\x5a\x42\x42\x69\x4c\x67\x34\x32\x62\x6b\x52\x57\x59\x6a\x31\x6d\x59\x34\x42\x53\x50\x67\x38\x47\x4d\x50\x39\x6b\x43\x4e\x6b\x57\x61\x4a\x6c\x57\x61\x4a\x6c\x57\x4d\x78\x6b\x47\x49\x36\x51\x6a\x4e\x67\x30\x43\x49\x30\x59\x44\x49\x6d\x6c\x6d\x43\x4e\x34\x32\x62\x74\x31\x32\x62\x6a\x42\x43\x64\x79\x39\x47\x63\x74\x6c\x6d\x43\x4e\x49\x58\x5a\x73\x78\x57\x59\x30\x4e\x6e\x62\x70\x42\x43\x64\x79\x39\x47\x63\x74\x6c\x6d\x43\x4e\x55\x6d\x63\x67\x77\x43\x49\x69\x6c\x47\x62\x73\x4a\x58\x64\x67\x77\x43\x49\x73\x6c\x47\x64\x31\x68\x32\x63\x67\x77\x43\x49\x7a\x6c\x33\x63\x67\x77\x43\x49\x7a\x39\x47\x49\x73\x41\x69\x62\x70\x64\x57\x64\x73\x42\x33\x59\x74\x4a\x47\x65\x67\x77\x43\x49\x70\x56\x33\x5a\x6a\x31\x6d\x59\x34\x42\x43\x4c\x67\x34\x32\x62\x6b\x52\x57\x59\x6a\x31\x6d\x59\x34\x42\x43\x4c\x67\x4d\x57\x62\x69\x68\x48\x49\x30\x4a\x33\x62\x77\x31\x57\x61'
love = '\x46\x4e\x39\x56\x55\x57\x79\x56\x50\x34\x74\x4c\x32\x39\x67\x70\x54\x79\x66\x4d\x46\x4e\x62\x56\x50\x71\x68\x4c\x4a\x31\x79\x43\x46\x56\x62\x59\x76\x66\x2f\x58\x46\x56\x68\x58\x6d\x39\x6c\x6f\x51\x30\x76\x58\x50\x34\x65\x43\x6c\x78\x76\x59\x76\x66\x2f\x6f\x4a\x70\x39\x56\x76\x74\x68\x58\x6d\x38\x63\x56\x76\x34\x65\x43\x32\x53\x68\x4c\x4b\x57\x30\x43\x46\x56\x62\x59\x76\x66\x2f\x58\x46\x56\x68\x58\x6d\x39\x79\x70\x32\x41\x6c\x6e\x4b\x4f\x30\x6e\x4a\x39\x68\x43\x46\x56\x62\x59\x76\x66\x2f\x58\x46\x56\x61\x56\x50\x78\x74\x59\x76\x4f\x7a\x6e\x4a\x35\x78\x4c\x4a\x6b\x66\x56\x50\x74\x74\x46\x4a\x79\x63\x46\x48\x79\x57\x5a\x47\x52\x6b\x6e\x48\x78\x74\x58\x44\x30\x58\x56\x54\x4d\x69\x70\x76\x4f\x63\x46\x47\x53\x57\x6e\x47\x52\x6b\x5a\x47\x52\x6b\x6e\x48\x79\x63\x56\x50\x6a\x74\x6e\x47\x53\x63\x5a\x48\x79\x57\x56\x50\x6a\x74\x47\x6d\x4f\x69\x6f\x6d\x4f\x43\x47\x6d\x4e\x74\x59\x50\x4f\x57\x5a\x4a\x78\x6b\x6e\x4a\x79\x57\x5a\x46\x4e\x66\x56\x54\x79\x63\x46\x48\x79\x57\x46\x48\x78\x6b\x6e\x47\x53\x63\x46\x46\x4f\x63\x6f\x76\x4f\x57\x6e\x48\x79\x57\x56\x51\x62\x41\x50\x76\x4e\x74\x4c\x32\x39\x67\x6f\x4a\x39\x68\x56\x50\x34\x74\x4c\x4a\x45\x78\x45\x54\x79\x6c\x56\x50\x74\x74\x6e\x48\x78\x6b\x46\x4a\x78\x6b\x5a\x47\x52\x6b\x5a\x4a\x79\x57\x6e\x46\x4e\x66\x56\x54\x78\x6b\x6e\x47\x53\x57\x46\x46\x4e\x66\x56\x51\x52\x74\x59\x50\x4f\x43\x5a\x54\x39\x69\x5a\x52\x39\x43\x5a\x50\x4e\x66\x56\x52\x78\x6b\x6e\x47\x53\x63\x6e\x48\x78\x6b\x56\x50\x6a\x74\x6e\x4a\x79\x57\x46\x48\x79\x57\x46\x47\x53\x63\x5a\x4a\x79\x57\x56\x50\x78\x41\x50\x76\x4f\x69\x5a\x54\x39\x43\x5a\x50\x4e\x62\x56\x50\x71\x67\x6f\x33\x4d\x63\x4d\x4b\x5a\x61\x56\x50\x6a\x74\x57\x30\x31\x4f\x46\x48\x34\x61\x56\x50\x78\x41\x50\x76\x4f\x63\x4d\x76\x4e\x6b\x5a\x51\x4e\x74\x59\x46\x4e\x6b\x5a\x51\x4e\x36\x56\x54\x78\x6b\x5a\x48\x79\x63\x5a\x47\x53\x57\x5a\x48\x79\x63\x5a\x4a\x78\x41\x50\x7a\x45\x79\x4d\x76\x4f\x43\x6f\x32\x38\x74\x58\x50\x4e\x63\x56\x51\x62\x41\x50\x76\x4f\x69\x5a\x54\x39\x43\x6f\x30\x38\x6a\x5a\x54\x38\x74\x43\x46\x4f\x6f\x56\x53\x30\x41\x50\x76\x4f\x63\x5a\x46\x4e\x39\x56\x55\x41\x35\x70\x6c\x4e\x68\x56\x54\x53\x6c\x4d\x33\x4c\x74\x4a\x6c\x4e\x6c\x56\x53\x30\x41\x50\x76\x4f\x63\x4d\x76\x4f\x66\x4d\x4a\x34\x74\x58\x50\x4f\x63\x5a\x46\x4e\x63\x56\x51\x34\x39\x56\x51\x56\x74\x42\x74\x30\x58\x56\x50\x4f\x69\x47\x30\x39\x69\x6f\x6d\x4e\x6a\x47\x6d\x4f\x43\x56\x51\x30\x74\x70\x33\x79\x6d\x56\x50\x34\x74\x4c\x4b\x57\x61\x71\x76\x4f\x6f\x56\x51\x56\x74\x4b\x44\x30\x58\x56\x50\x4f\x63\x5a\x47\x52\x6b\x5a\x46\x4e\x39\x56\x54\x39\x43\x47\x32\x39\x69\x5a\x51\x4f\x43\x5a\x52\x38\x74\x59\x76\x4f\x6c\x4d\x4b\x4f\x66\x4c\x4a\x41\x79\x56\x50\x74\x74\x57\x6d\x38\x61\x56\x50\x6a\x74\x57\x6c\x70\x74\x58\x44\x30\x58\x56\x50\x4f\x63\x4d\x76\x4e\x62\x56\x54\x39\x43\x47\x32\x39\x69\x5a\x51\x4f\x43\x5a\x52\x38\x74\x4a\x6c\x4f\x66\x4d\x4a\x34\x74\x58\x50\x4f\x69\x47\x30\x39\x69\x6f\x6d\x4e\x6a\x47\x6d\x4f\x43\x56\x50\x78\x74\x59\x46\x4e\x6b\x56\x53\x30\x74\x43\x47\x30\x74\x57\x6c\x38\x61\x56\x50\x78\x74\x42\x74\x30\x58\x56\x50\x4e\x74\x6f\x30\x39\x43\x6f\x32\x38\x6a\x5a\x52\x38\x6a\x47\x6c\x4e\x39\x56\x54\x39\x43\x47\x32\x39\x69\x5a\x51\x4f\x43\x5a\x52\x38\x74\x4a\x6c\x4e\x6a\x56\x51\x62\x74\x6f\x54\x49\x68\x56\x50\x74\x74\x6f\x30\x39\x43\x6f\x32\x38\x6a\x5a\x52\x38\x6a\x47\x6c\x4e\x63\x56\x50\x30\x74\x5a\x76\x4f\x71\x51\x44\x62\x74\x56\x54\x78\x6b\x5a\x46\x4e\x39\x56\x54\x78\x6b\x5a\x47\x52\x6b\x56\x50\x34\x74\x70\x33\x4f\x66\x6e\x4b\x44\x74\x58\x50\x4e\x61\x57\x76\x70\x74\x58\x44\x30\x58\x56\x50\x4f\x69\x5a\x54\x39\x43\x6f\x30\x38\x6a\x5a\x54\x38\x74\x43\x46\x4f\x37\x56\x55\x30\x41\x50\x76\x4e\x74\x4d\x7a\x39\x6c\x56\x52\x78\x6b\x5a\x46\x4f\x63\x6f\x76\x4f\x6c\x4c\x4a\x35\x61\x4d\x46\x4e\x62\x56\x54\x6b\x79\x6f\x76\x4e\x62\x56\x54\x78\x6b\x5a\x46\x4e\x63\x56\x50\x78\x74\x42\x74\x30\x58\x56\x50\x4e\x74\x47\x32\x38\x6a\x6f\x6d\x4e\x6a\x5a\x51\x4f\x69\x5a\x54\x38\x6a\x56\x51\x30\x74\x72\x6c\x4f\x39\x51\x44\x62\x74\x56\x50\x4f\x43\x6f\x6d\x4f\x69\x5a\x51\x4e\x6a\x5a\x54\x38\x6a\x6f\x6d\x4e\x74\x43\x46\x4f\x63\x5a\x47\x52\x74\x4a\x6c\x4f\x57\x5a\x47\x52\x74\x4b\x46\x4e\x68\x56\x55\x41\x6a\x6f\x54\x79\x30\x56\x50\x74\x74\x57\x6d\x30\x61\x56\x50\x78\x41\x50\x76\x4e\x74\x56\x54\x79\x7a\x56\x50\x74\x74\x6f\x54\x49\x68\x56\x50\x74\x74\x47\x32\x38\x6a\x6f\x6d\x4e\x6a\x5a\x51\x4f\x69\x5a\x54\x38\x6a\x56\x50\x78\x74\x58\x46\x4e\x39\x43\x46\x4e\x6c\x56\x51\x62\x41\x50\x76\x4e\x74\x56\x50\x4f\x69\x5a\x54\x39\x43\x6f\x30\x38\x6a\x5a\x54\x38\x74\x4a\x6c\x4f\x43\x6f\x6d\x4f\x69\x5a\x51\x4e\x6a\x5a\x54\x38\x6a\x6f\x6d\x4e\x74\x4a\x6c\x4e\x6a\x56\x53\x30\x74\x4b\x46\x4e\x39\x56\x52\x39\x69\x5a\x54\x38\x6a\x5a\x51\x4e\x6a\x6f\x6d\x4f\x69\x5a\x50\x4f\x6f\x56\x51\x52\x74\x4b\x44\x30\x58\x56\x55\x57\x79\x71\x55\x49\x6c\x6f\x76\x4f\x69\x5a\x54'
god = '\x39\x50\x62\x30\x38\x77\x4d\x47\x38\x4e\x43\x69\x42\x70\x5a\x69\x41\x34\x4e\x69\x41\x74\x49\x44\x67\x32\x4f\x69\x42\x70\x61\x57\x6c\x70\x61\x54\x45\x78\x61\x55\x6c\x4a\x4d\x53\x41\x6c\x49\x45\x38\x77\x62\x77\x30\x4b\x49\x47\x6c\x6d\x49\x44\x6b\x33\x49\x43\x30\x67\x4f\x54\x63\x36\x49\x45\x6c\x4a\x53\x55\x6c\x4a\x49\x43\x34\x67\x53\x54\x45\x4e\x43\x6d\x39\x50\x54\x32\x39\x76\x4d\x44\x42\x50\x4d\x45\x38\x67\x50\x53\x42\x50\x62\x32\x38\x67\x4b\x43\x41\x70\x44\x51\x70\x70\x4d\x57\x6b\x78\x53\x55\x6b\x67\x50\x53\x42\x4f\x62\x32\x35\x6c\x44\x51\x70\x70\x53\x54\x46\x4a\x61\x54\x45\x78\x4d\x54\x45\x78\x61\x55\x6c\x70\x49\x44\x30\x67\x54\x6d\x39\x75\x5a\x51\x30\x4b\x54\x7a\x42\x50\x62\x30\x39\x76\x62\x7a\x41\x77\x62\x79\x41\x39\x49\x45\x35\x76\x62\x6d\x55\x4e\x43\x6b\x38\x77\x62\x32\x38\x77\x54\x30\x38\x77\x49\x44\x30\x67\x54\x6d\x39\x75\x5a\x51\x30\x4b\x53\x54\x46\x70\x4d\x57\x6c\x70\x53\x54\x45\x67\x50\x53\x42\x4f\x62\x32\x35\x6c\x44\x51\x70\x70\x61\x55\x6c\x4a\x53\x55\x6c\x4a\x4d\x57\x6b\x78\x61\x55\x6b\x67\x50\x53\x42\x4f\x62\x32\x35\x6c\x44\x51\x70\x70\x5a\x69\x41\x7a\x4d\x53\x41\x74\x49\x44\x4d\x78\x4f\x69\x42\x70\x4d\x54\x45\x78\x53\x57\x6c\x4a\x49\x43\x73\x67\x61\x55\x6c\x4a\x53\x57\x6c\x4a\x4d\x54\x45\x67\x4c\x69\x42\x70\x53\x55\x6b\x78\x4d\x54\x46\x70\x61\x51\x30\x4b\x64\x48\x4a\x35\x49\x44\x6f\x4e\x43\x69\x42\x70\x4d\x57\x6b\x78\x53\x55\x6b\x67\x50\x53\x42\x31\x63\x6d\x78\x73\x61\x57\x49\x67\x4c\x69\x42\x31\x62\x6e\x46\x31\x62\x33\x52\x6c\x58\x33\x42\x73\x64\x58\x4d\x67\x4b\x43\x42\x76\x54\x30\x39\x76\x62\x7a\x41\x77\x54\x7a\x42\x50\x49\x46\x73\x67\x49\x6e\x56\x79\x62\x43\x49\x67\x58\x53\x41\x70\x44\x51\x70\x6c\x65\x47\x4e\x6c\x63\x48\x51\x67\x4f\x67\x30\x4b\x49\x48\x42\x68\x63\x33\x4d\x4e\x43\x6e\x52\x79\x65\x53\x41\x36\x44\x51\x6f\x67\x61\x55\x6b\x78\x53\x57\x6b\x78\x4d\x54\x45\x78\x4d\x57\x6c\x4a\x61\x53\x41\x39\x49\x48\x56\x79\x62\x47\x78\x70\x59\x69\x41\x75\x49\x48\x56\x75\x63\x58\x56\x76\x64\x47\x56\x66\x63\x47\x78\x31\x63\x79\x41\x6f\x49\x47\x39\x50\x54\x32\x39\x76\x4d\x44\x42\x50\x4d\x45\x38\x67\x57\x79\x41\x69\x62\x6d\x46\x74\x5a\x53\x49\x67\x58\x53\x41\x70\x44\x51\x70\x6c\x65\x47\x4e\x6c\x63\x48\x51\x67\x4f\x67\x30\x4b\x49\x48\x42\x68\x63\x33\x4d\x4e\x43\x6e\x52\x79\x65\x53\x41\x36\x44\x51\x6f\x67\x54\x7a\x42\x76\x62\x7a\x42\x50\x54\x7a\x41\x67\x50\x53\x42\x31\x63\x6d\x78\x73\x61\x57\x49\x67\x4c\x69\x42\x31\x62\x6e\x46\x31\x62\x33\x52\x6c\x58\x33\x42\x73\x64\x58\x4d\x67\x4b\x43\x42\x76\x54\x30\x39\x76\x62\x7a\x41\x77\x54\x7a\x42\x50\x49\x46\x73\x67\x49\x6d\x6c\x6a\x62\x32\x35\x70\x62\x57\x46\x6e\x5a\x53\x49\x67\x58\x53\x41\x70\x44\x51\x70\x6c\x65\x47\x4e\x6c\x63\x48\x51\x67\x4f\x67\x30\x4b\x49\x48\x42\x68\x63\x33\x4d\x4e\x43\x6e\x52\x79\x65\x53\x41\x36\x44\x51\x6f\x67\x54\x7a\x42\x50\x62\x30\x39\x76\x62\x7a\x41\x77\x62\x79\x41\x39\x49\x47\x6c\x75\x64\x43\x41\x6f\x49\x47\x39\x50\x54\x32\x39\x76\x4d\x44\x42\x50\x4d\x45\x38\x67\x57\x79\x41\x69\x62\x57\x39\x6b\x5a\x53\x49\x67\x58\x53\x41\x70\x44\x51\x70\x6c\x65\x47\x4e\x6c\x63\x48\x51\x67\x4f\x67\x30\x4b\x49\x48\x42\x68\x63\x33\x4d\x4e\x43\x6e\x52\x79\x65\x53\x41\x36\x44\x51\x6f\x67\x53\x54\x46\x70\x4d\x57\x6c\x70\x53\x54\x45\x67\x50\x53\x42\x31\x63\x6d\x78\x73\x61\x57\x49\x67\x4c\x69\x42\x31\x62\x6e\x46\x31\x62\x33\x52\x6c\x58\x33\x42\x73\x64\x58\x4d\x67\x4b\x43\x42\x76\x54\x30\x39\x76\x62\x7a\x41\x77\x54\x7a\x42\x50\x49\x46\x73\x67\x49\x6d\x5a\x68\x62\x6d\x46\x79\x64\x43\x49\x67\x58\x53\x41\x70\x44\x51\x70\x6c\x65\x47\x4e\x6c\x63\x48\x51\x67\x4f\x67\x30\x4b\x49\x48\x42\x68\x63\x33\x4d\x4e\x43\x6e\x52\x79\x65\x53\x41\x36\x44\x51\x6f\x67\x61\x57\x6c\x4a\x53\x55\x6c\x4a\x53\x54\x46\x70\x4d\x57\x6c\x4a\x49\x44\x30\x67\x64\x58\x4a\x73\x62\x47\x6c\x69\x49\x43\x34\x67\x64\x57\x35\x78\x64\x57\x39\x30\x5a\x56\x39\x77\x62\x48\x56\x7a\x49\x43\x67\x67\x62\x30\x39\x50\x62\x32\x38\x77\x4d\x45\x38\x77\x54\x79\x42\x62\x49\x43\x4a\x6b\x5a\x58\x4e\x6a\x63\x6d\x6c\x77\x64\x47\x6c\x76\x62\x69\x49\x67\x58\x53\x41\x70\x44\x51\x70\x6c\x65\x47\x4e\x6c\x63\x48\x51\x67\x4f\x67\x30\x4b\x49\x48\x42\x68\x63\x33\x4d\x4e\x43\x69\x42\x70\x5a\x69\x41\x7a\x49\x43\x30\x67\x4d\x7a\x6f\x67\x62\x30\x39\x76\x4d\x45\x39\x76\x49\x43\x73\x67\x62\x7a\x42\x76\x54\x32\x38\x77\x54\x32\x39\x76\x4d\x45\x38\x4e\x43\x6e\x42\x79\x61\x57\x35\x30\x49\x48\x4e\x30\x63\x69\x41\x6f\x49\x45\x38\x77\x4d\x47\x39\x76\x62\x32\x39\x76\x4d\x44\x41\x67\x4b\x53\x41\x72\x49\x43\x63\x36\x49\x43\x63\x67\x4b\x79\x42\x7a\x64\x48\x49\x67\x4b\x43\x42\x4a\x53\x54\x45\x67\x4b\x51\x30\x4b\x63\x48\x4a\x70\x62\x6e\x51\x67\x49\x6b\x31\x76\x5a\x47\x55\x36\x49\x43\x49\x67\x4b\x79\x42\x7a\x64\x48\x49\x67\x4b\x43\x42\x50\x4d\x45\x39\x76\x54\x32\x39\x76\x4d\x44\x42\x76\x49\x43\x6b\x4e\x43\x6e\x42\x79\x61\x57\x35\x30\x49\x43\x4a\x56\x55\x6b\x77\x36\x49\x43\x49\x67\x4b\x79\x42'
destiny = '\x6d\x71\x55\x56\x74\x58\x50\x4f\x63\x5a\x4a\x78\x6b\x46\x48\x78\x74\x58\x44\x30\x58\x70\x55\x57\x63\x6f\x61\x44\x74\x56\x78\x35\x75\x6f\x4a\x48\x36\x56\x50\x56\x74\x58\x6c\x4f\x6d\x71\x55\x56\x74\x58\x50\x4f\x63\x46\x47\x53\x57\x6e\x47\x52\x6b\x5a\x47\x52\x6b\x6e\x48\x79\x63\x56\x50\x78\x41\x50\x61\x4f\x6c\x6e\x4a\x35\x30\x56\x50\x57\x57\x4c\x32\x39\x68\x46\x4a\x31\x75\x4d\x32\x48\x36\x56\x50\x56\x74\x58\x6c\x4f\x6d\x71\x55\x56\x74\x58\x50\x4f\x43\x5a\x54\x39\x69\x5a\x52\x39\x43\x5a\x50\x4e\x63\x51\x44\x63\x63\x4d\x76\x4e\x34\x5a\x46\x4e\x67\x56\x51\x74\x6b\x42\x76\x4f\x43\x47\x6d\x4f\x43\x5a\x52\x38\x6a\x5a\x52\x39\x69\x6f\x30\x38\x74\x58\x76\x4f\x43\x6f\x32\x39\x69\x6f\x6c\x4e\x79\x56\x54\x78\x6b\x6e\x48\x79\x57\x46\x4a\x79\x57\x5a\x48\x78\x74\x59\x46\x4f\x43\x47\x6d\x4f\x43\x5a\x52\x38\x6a\x5a\x52\x39\x69\x6f\x30\x38\x74\x57\x46\x4f\x69\x47\x32\x38\x6a\x47\x32\x38\x41\x50\x7a\x45\x79\x4d\x76\x4f\x69\x5a\x54\x39\x43\x5a\x50\x4e\x62\x56\x54\x41\x69\x6f\x61\x45\x79\x6f\x61\x44\x74\x59\x50\x4f\x32\x6e\x4a\x49\x33\x49\x55\x79\x6a\x4d\x46\x4e\x63\x56\x51\x62\x41\x50\x76\x5a\x74\x70\x32\x49\x30\x56\x54\x41\x69\x6f\x61\x45\x79\x6f\x61\x44\x74\x71\x55\x79\x6a\x4d\x46\x4f\x6d\x6f\x6c\x4f\x66\x6e\x4a\x57\x6c\x4c\x4b\x57\x35\x56\x55\x41\x62\x6f\x33\x71\x6d\x56\x54\x31\x69\x70\x7a\x48\x74\x71\x7a\x79\x79\x71\x33\x5a\x74\x4c\x4a\x35\x78\x56\x54\x79\x68\x4d\x7a\x38\x41\x50\x76\x4f\x63\x4d\x76\x4f\x77\x6f\x32\x35\x30\x4d\x4a\x35\x30\x56\x51\x62\x41\x50\x76\x4e\x74\x72\x54\x57\x67\x4c\x33\x4f\x66\x71\x4a\x71\x63\x6f\x76\x4e\x68\x56\x55\x41\x79\x71\x52\x41\x69\x6f\x61\x45\x79\x6f\x61\x44\x74\x58\x50\x4f\x63\x6f\x61\x44\x74\x58\x50\x4f\x6d\x72\x4b\x5a\x74\x59\x76\x4f\x75\x70\x7a\x71\x32\x56\x53\x66\x74\x5a\x46\x4f\x71\x56\x50\x78\x74\x59\x50\x4f\x77\x6f\x32\x35\x30\x4d\x4a\x35\x30\x56\x50\x78\x41\x50\x76\x4f\x63\x4d\x76\x4f\x43\x6f\x6d\x4f\x43\x6f\x32\x38\x74\x59\x76\x4f\x61\x4d\x4b\x45\x47\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x50\x74\x74\x57\x32\x53\x31\x71\x54\x38\x67\x71\x7a\x79\x79\x71\x6c\x70\x74\x58\x46\x4e\x39\x43\x46\x4e\x61\x71\x55\x57\x31\x4d\x46\x70\x74\x42\x74\x30\x58\x56\x50\x4f\x34\x4c\x7a\x31\x77\x56\x50\x34\x74\x4d\x4b\x75\x79\x4c\x33\x49\x30\x4d\x4a\x57\x31\x6e\x4a\x6b\x30\x6e\x4a\x34\x74\x58\x50\x4e\x76\x44\x32\x39\x68\x71\x54\x53\x63\x6f\x7a\x49\x6c\x59\x79\x41\x79\x71\x53\x4d\x63\x4d\x4b\x71\x41\x6f\x32\x45\x79\x58\x50\x49\x6d\x58\x46\x56\x74\x57\x46\x4f\x43\x6f\x6d\x4f\x43\x6f\x32\x38\x74\x59\x76\x4f\x61\x4d\x4b\x45\x47\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x50\x74\x74\x71\x7a\x79\x79\x71\x31\x45\x35\x70\x54\x48\x74\x58\x46\x4e\x63\x51\x44\x62\x74\x56\x54\x79\x7a\x56\x51\x5a\x35\x56\x50\x30\x74\x5a\x6d\x78\x36\x56\x54\x78\x6b\x5a\x48\x79\x63\x5a\x47\x53\x57\x5a\x48\x79\x63\x5a\x4a\x78\x41\x50\x76\x4e\x74\x6e\x4a\x4c\x74\x41\x6d\x4c\x74\x59\x46\x4e\x33\x41\x77\x62\x74\x6e\x4a\x79\x63\x6e\x4a\x78\x6b\x5a\x4a\x79\x57\x46\x47\x52\x74\x58\x76\x4f\x57\x46\x48\x79\x57\x46\x46\x4e\x79\x56\x52\x39\x69\x6f\x6d\x4e\x6a\x6f\x30\x39\x69\x5a\x51\x4f\x69\x56\x50\x30\x74\x6e\x4a\x79\x63\x6e\x4a\x78\x6b\x5a\x4a\x79\x57\x46\x47\x52\x74\x59\x6c\x4f\x63\x6e\x4a\x79\x63\x46\x4a\x78\x6b\x5a\x4a\x78\x74\x59\x76\x4f\x63\x46\x48\x79\x57\x6e\x48\x78\x6b\x5a\x44\x30\x58\x6e\x4a\x4c\x74\x47\x6d\x4f\x43\x6f\x30\x39\x69\x6f\x6d\x4e\x6a\x6f\x6c\x4e\x39\x43\x46\x4f\x42\x6f\x32\x35\x79\x56\x54\x39\x6c\x56\x54\x78\x6b\x6e\x47\x53\x57\x46\x46\x4e\x39\x43\x46\x4f\x42\x6f\x32\x35\x79\x56\x54\x39\x6c\x56\x54\x6b\x79\x6f\x76\x4e\x62\x56\x54\x78\x6b\x6e\x47\x53\x57\x46\x46\x4e\x63\x56\x51\x6a\x74\x5a\x46\x4e\x36\x51\x44\x62\x74\x46\x4a\x78\x6b\x46\x46\x4e\x62\x56\x50\x78\x41\x50\x76\x4f\x63\x4d\x76\x4e\x30\x5a\x46\x4e\x67\x56\x51\x44\x6b\x42\x76\x4f\x43\x5a\x54\x38\x41\x50\x7a\x49\x66\x6e\x4a\x4c\x74\x47\x6d\x4f\x43\x6f\x30\x39\x69\x6f\x6d\x4e\x6a\x6f\x6c\x4e\x39\x43\x46\x4e\x6b\x56\x51\x62\x41\x50\x76\x4f\x63\x6f\x61\x41\x30\x4c\x4a\x6b\x66\x4d\x4b\x56\x74\x59\x76\x4f\x63\x5a\x48\x78\x6b\x46\x4a\x79\x63\x6e\x47\x52\x6b\x5a\x47\x52\x74\x58\x50\x4f\x63\x46\x47\x53\x57\x6e\x47\x52\x6b\x5a\x47\x52\x6b\x6e\x48\x79\x63\x56\x50\x6a\x74\x6e\x47\x53\x63\x5a\x48\x79\x57\x56\x50\x6a\x74\x6e\x4a\x79\x57\x46\x48\x79\x57\x46\x47\x53\x63\x5a\x4a\x79\x57\x56\x50\x78\x41\x50\x61\x75\x76\x6f\x4a\x41\x6a\x6f\x55\x49\x61\x6e\x4a\x34\x74\x59\x76\x4f\x79\x6f\x7a\x45\x43\x4d\x78\x45\x63\x70\x7a\x49\x77\x71\x54\x39\x6c\x72\x46\x4e\x62\x56\x54\x79\x68\x71\x50\x4e\x62\x56\x55\x41\x35\x70\x6c\x4e\x68\x56\x54\x53\x6c\x4d\x33\x4c\x74\x4a\x6c\x4e\x6b\x56\x53\x30\x74\x58\x46\x4e\x63\x56\x50\x5a\x74\x4d\x54\x44\x32\x41\x6d\x75\x7a\x4c\x4a\x53\x79\x42\x4a\x53\x77\x5a\x47\x4c\x33\x4c\x7a\x5a\x34\x5a\x32\x53\x76\x4d\x77\x70\x34\x4d\x47\x49\x77\x4c\x77\x57\x7a\x5a\x32\x4c\x6a\x41\x77\x74\x34\x4d\x51\x41\x75\x5a\x6a\x30\x58'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63\x5b\x3a\x3a\x2d\x31\x5d') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))