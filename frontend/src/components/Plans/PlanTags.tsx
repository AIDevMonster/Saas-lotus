import React from "react";
import { components } from "../../gen-types";
import Badge from "../base/Badges/Badges";

interface PlanTagsProps {
  tags:
    | components["schemas"]["PlanDetail"]["tags"]
    | components["schemas"]["Plan"]["tags"];
  showAddTagButton?: boolean;
}

function PlansTags({ tags, showAddTagButton }: PlanTagsProps) {
  return (
    <span>
      {!tags.length && !((import.meta as any).env.VITE_IS_DEMO === "true") ? (
        <Badge className="bg-[#E0E7FF] text-[#3730A3] text-[12px] px-[6px] py-2">
          <Badge.Content>+ Add Tag</Badge.Content>
        </Badge>
      ) : (
        <span className="flex">
          <span className="flex">
            {tags.length >= 3 ? (
              <span className="flex gap-2">
                {tags.slice(0, 2).map((tag) => (
                  <span className="flex gap-2" key={tag.tag_name}>
                    <Badge className="text-[12px] px-[5px] py-0.5 bg-white text-black whitespace-nowrap">
                      <div className="flex gap-2 items-center">
                        <Badge.Dot fill={tag.tag_hex} />
                        <Badge.Content>{tag.tag_name}</Badge.Content>
                      </div>
                    </Badge>
                  </span>
                ))}
                <span className="whitespace-nowrap">
                  {" "}
                  +{tags.length - tags.slice(0, 2).length}{" "}
                  {tags.length - tags.slice(0, 2).length > 1 ? "tags" : "tag"}
                </span>
              </span>
            ) : (
              tags.map((tag) => (
                <span key={tag.tag_name} className="flex gap-2">
                  <span className="flex gap-2" key={tag.tag_name}>
                    <Badge className="text-[12px] px-[5px] py-2 bg-white text-black whitespace-nowrap">
                      <div className="flex gap-2 items-center">
                        <Badge.Dot fill={tag.tag_hex} />
                        <Badge.Content>{tag.tag_name}</Badge.Content>
                      </div>
                    </Badge>
                  </span>
                </span>
              ))
            )}
            {showAddTagButton &&
              !((import.meta as any).env.VITE_IS_DEMO === "true") &&
              tags.length < 3 && (
                <Badge className="bg-[#E0E7FF] text-[#3730A3] text-[12px] px-[6px] py-2 ml-2 whitespace-nowrap">
                  <Badge.Content>+ Add Tag</Badge.Content>
                </Badge>
              )}
          </span>
        </span>
      )}
    </span>
  );
}
export default PlansTags;
