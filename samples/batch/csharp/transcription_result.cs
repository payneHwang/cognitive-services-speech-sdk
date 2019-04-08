﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BatchClient
{
    public class AudioFileResult
    {
        public string AudioFileName { get; set; }
        public List<SegmentResult> SegmentResults { get; set; }
    }

    public class RootObject
    {
        public List<AudioFileResult> AudioFileResults { get; set; }
    }

    public class NBest
    {
        public double Confidence { get; set; }
        public string Lexical { get; set; }
        public string ITN { get; set; }
        public string MaskedITN { get; set; }
        public string Display { get; set; }
    }

    public class SegmentResult
    {
        public string RecognitionStatus { get; set; }
        public string Offset { get; set; }
        public string Duration { get; set; }
        public List<NBest> NBest { get; set; }
    }
}

