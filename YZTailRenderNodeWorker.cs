using RimWorld;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;
using UnityEngine;
using Verse;

namespace twcyz
{
    public class YZTailAllFixRenderNodeWorker : PawnRenderNodeWorker
    {
        public override Vector3 OffsetFor(PawnRenderNode node, PawnDrawParms parms, out Vector3 pivot)
        {
            Vector3 result = base.OffsetFor(node, parms, out pivot);
            if (parms.pawn.story != null)
            {
                if (parms.pawn.story.bodyType != BodyTypeDefOf.Female)
                {
                    if (parms.facing == Rot4.East)
                        result.x += 0.07f;
                    else if (parms.facing == Rot4.West)
                        result.x -= 0.07f;
                }
                if (parms.pawn.story.bodyType == BodyTypeDefOf.Baby || parms.pawn.story.bodyType == BodyTypeDefOf.Child)
                    result.z += 0.04f;
            }
            return result;
        }
    }
    public class YZTailChildFixRenderNodeWorker : PawnRenderNodeWorker
    {
        public override Vector3 OffsetFor(PawnRenderNode node, PawnDrawParms parms, out Vector3 pivot)
        {
            Vector3 result = base.OffsetFor(node, parms, out pivot);
            if (parms.pawn.story != null)
            {
                if (parms.pawn.story.bodyType == BodyTypeDefOf.Baby || parms.pawn.story.bodyType == BodyTypeDefOf.Child)
                {
                    if (parms.facing == Rot4.East)
                        result.x += 0.07f;
                    else if (parms.facing == Rot4.West)
                        result.x -= 0.07f;
                    result.z += 0.04f;
                }
            }
            return result;
        }
    }
}
